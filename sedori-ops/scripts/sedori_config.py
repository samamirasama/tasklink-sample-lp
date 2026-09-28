"""共通: business.yaml と FBA手数料表の読み込み。

PyYAML があればそれを使い、無ければ business.yaml で使っている YAML の部分集合
（ネストしたマップ、スカラーのリスト、マップのリスト、コメント、引用符付き文字列）
だけを解釈する簡易パーサにフォールバックします。標準ライブラリのみで動作します。

使い方:
    from sedori_config import load_config, load_fba_fees, repo_path
    cfg = load_config()
    print(cfg["targets"]["roi_min"])
"""
from __future__ import annotations

import csv
import os
import re
from typing import Any

HERE = os.path.dirname(os.path.abspath(__file__))
OPS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
REPO_ROOT = os.path.abspath(os.path.join(OPS_ROOT, ".."))
CONFIG_PATH = os.path.join(OPS_ROOT, "config", "business.yaml")


def repo_path(rel: str) -> str:
    """リポジトリルートからの相対パスを絶対パスにする。"""
    return os.path.join(REPO_ROOT, rel)


# ---------------------------------------------------------------------------
# 簡易 YAML パーサ（フォールバック）
# ---------------------------------------------------------------------------
_SCALAR_INT = re.compile(r"^-?\d+$")
_SCALAR_FLOAT = re.compile(r"^-?\d+\.\d+$")


def _strip_comment(line: str) -> str:
    """引用符の外にある # 以降を落とす。"""
    out = []
    quote = None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            out.append(ch)
        elif ch == "#":
            break
        else:
            out.append(ch)
    return "".join(out).rstrip()


def _parse_scalar(text: str) -> Any:
    t = text.strip()
    if t == "" or t in ("null", "~"):
        return None
    if len(t) >= 2 and t[0] == t[-1] and t[0] in ("'", '"'):
        return t[1:-1]
    if t in ("true", "True"):
        return True
    if t in ("false", "False"):
        return False
    if _SCALAR_INT.match(t):
        return int(t)
    if _SCALAR_FLOAT.match(t):
        return float(t)
    return t


def _split_key(text: str) -> tuple[str, str] | None:
    """`key: value` を分割。引用符付きキーにも対応。"""
    m = re.match(r'^\s*("([^"]*)"|\'([^\']*)\'|([^:#]+?))\s*:(?:\s+(.*))?$', text)
    if not m:
        return None
    key = m.group(2) or m.group(3) or m.group(4)
    return key.strip(), (m.group(5) or "").strip()


def _parse_lines(lines: list[str]) -> Any:
    """インデント付きの行リストを再帰的に解釈する。"""
    items = [(len(l) - len(l.lstrip(" ")), l.strip()) for l in lines if l.strip()]
    if not items:
        return None
    return _parse_block(items, 0, len(items), items[0][0])[0]


def _parse_block(items, start, end, indent):
    first = items[start][1]
    if first.startswith("- "):
        return _parse_list(items, start, end, indent)
    return _parse_map(items, start, end, indent)


def _parse_map(items, start, end, indent):
    result: dict[str, Any] = {}
    i = start
    while i < end:
        ind, text = items[i]
        if ind < indent:
            break
        if ind > indent:
            raise ValueError(f"YAML: unexpected indent near: {text}")
        kv = _split_key(text)
        if kv is None:
            raise ValueError(f"YAML: expected 'key: value' near: {text}")
        key, value = kv
        j = i + 1
        while j < end and items[j][0] > indent:
            j += 1
        if value == "":
            if j > i + 1:
                result[key] = _parse_block(items, i + 1, j, items[i + 1][0])[0]
            else:
                result[key] = None
        else:
            result[key] = _parse_scalar(value)
        i = j
    return result, i


def _parse_list(items, start, end, indent):
    result: list[Any] = []
    i = start
    while i < end:
        ind, text = items[i]
        if ind < indent:
            break
        if ind > indent or not text.startswith("- "):
            raise ValueError(f"YAML: expected list item near: {text}")
        body = text[2:].strip()
        j = i + 1
        while j < end and items[j][0] > indent:
            j += 1
        kv = _split_key(body) if body and not body.startswith(("'", '"')) else None
        if kv is not None:
            # `- key: value` 形式: 続く行と合わせてマップにする
            key, value = kv
            sub_items = [(indent + 2, body)] + [items[k] for k in range(i + 1, j)]
            # 続く行のインデントは indent+2 に揃っている想定
            mapping, _ = _parse_map(sub_items, 0, len(sub_items), sub_items[0][0])
            result.append(mapping)
        else:
            result.append(_parse_scalar(body))
        i = j
    return result, i


def _load_yaml_text(text: str) -> Any:
    try:
        import yaml  # type: ignore

        return yaml.safe_load(text)
    except ImportError:
        lines = [_strip_comment(l) for l in text.splitlines()]
        return _parse_lines(lines)


# ---------------------------------------------------------------------------
# 公開API
# ---------------------------------------------------------------------------
def load_config(path: str = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        cfg = _load_yaml_text(f.read())
    if not isinstance(cfg, dict):
        raise ValueError("business.yaml のトップレベルはマップである必要があります")
    return cfg


def load_fba_fees(cfg: dict) -> dict[str, dict]:
    """サイズ区分 -> {fee_jpy, verified_on, ...} を返す。fee_jpy が 0 のものは未設定扱い。"""
    rel = cfg["selling_platforms"]["amazon"].get("fba_fulfillment_fee_table", "")
    path = repo_path(rel) if rel else ""
    fees: dict[str, dict] = {}
    if not path or not os.path.exists(path):
        return fees
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            tier = (row.get("size_tier") or "").strip()
            if not tier:
                continue
            try:
                fee = int(float(row.get("fee_jpy") or 0))
            except ValueError:
                fee = 0
            fees[tier] = {
                "fee_jpy": fee,
                "verified_on": (row.get("verified_on") or "").strip(),
            }
    return fees


def referral_rate(cfg: dict, category: str | None) -> tuple[float, str]:
    """カテゴリ別販売手数料率と、その出所（category / default）を返す。"""
    amz = cfg["selling_platforms"]["amazon"]
    by_cat = amz.get("referral_fee_by_category") or {}
    if category and category in by_cat:
        return float(by_cat[category]), "category"
    return float(amz.get("referral_fee_default", 0.15)), "default"


if __name__ == "__main__":
    import json

    c = load_config()
    print(json.dumps({"last_updated": c.get("last_updated"), "targets": c.get("targets")}, ensure_ascii=False, indent=2))
    print("fba fee tiers:", list(load_fba_fees(c).keys()))
