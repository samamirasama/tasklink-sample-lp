#!/usr/bin/env python3
"""試用データの集計（03_検証計画.md 7章の定義に対応）。

入力: events.jsonl（1行1イベント）。各行は {"user":"U1","ts":"2026-10-20T09:00:00","event":"capture_attempt","attrs":{...}}
使い方: python3 compute_metrics.py events.jsonl [--window-days 14]
出力: 参加者ごとの指標と全体値。分母を必ず併記する。
"""
import json, sys, argparse
from collections import defaultdict
from datetime import datetime, timedelta

def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            r["ts"] = datetime.fromisoformat(r["ts"])
            r.setdefault("attrs", {})
            rows.append(r)
    return rows

def metrics(rows, window_days):
    by_user = defaultdict(list)
    for r in rows:
        by_user[r["user"]].append(r)
    out = {}
    for u, evs in by_user.items():
        evs.sort(key=lambda r: r["ts"])
        start = evs[0]["ts"]
        win_end = start + timedelta(days=window_days)
        day7 = start + timedelta(days=7)
        att = sum(1 for r in evs if r["event"] == "capture_attempt")
        ok = sum(1 for r in evs if r["event"] == "capture_success")
        first_day_saves = sum(1 for r in evs if r["event"] == "capture_success" and r["ts"] < start + timedelta(days=1))
        # 7日後利用：7日目±1日に保存またはレビュー操作
        d7 = any(r["event"] in ("capture_success", "review_start", "item_resolve") and abs((r["ts"] - day7).days) <= 1 for r in evs)
        # 保存コホート：観察期間内に保存した件数（item id は attrs.item）
        saved = {r["attrs"].get("item") for r in evs if r["event"] == "capture_success" and r["ts"] <= win_end}
        saved.discard(None)
        opened = {r["attrs"].get("item") for r in evs if r["event"] == "item_open" and r["ts"] <= win_end and r["attrs"].get("item") in saved}
        done = {r["attrs"].get("item") for r in evs if r["event"] == "item_resolve" and r["attrs"].get("status") == "done" and r["ts"] <= win_end and r["attrs"].get("item") in saved}
        dismissed = {r["attrs"].get("item") for r in evs if r["event"] == "item_resolve" and r["attrs"].get("status") == "dismissed" and r["ts"] <= win_end and r["attrs"].get("item") in saved}
        notif_granted = any(r["event"] == "notif_permission" and r["attrs"].get("granted") for r in evs)
        notif_disabled = any(r["event"] == "notif_disabled" for r in evs)
        reviews = sum(1 for r in evs if r["event"] == "review_start")
        n = len(saved)
        out[u] = {
            "保存成功率": f"{ok}/{att}" + (f" ({ok/att:.0%})" if att else ""),
            "初日3件以上": first_day_saves >= 3,
            "7日後利用": d7,
            "再利用率": f"{len(opened)}/{n}" + (f" ({len(opened)/n:.0%})" if n else ""),
            "実行率": f"{len(done)}/{n}" + (f" ({len(done)/n:.0%})" if n else ""),
            "整理率": f"{len(done|dismissed)}/{n}" + (f" ({len(done|dismissed)/n:.0%})" if n else ""),
            "週次レビュー回数": reviews,
            "通知": "未許可" if not notif_granted else ("許可→無効化" if notif_disabled else "許可のまま"),
        }
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--window-days", type=int, default=14)
    a = ap.parse_args()
    res = metrics(load(a.path), a.window_days)
    users = sorted(res)
    print(f"観察期間: 開始から{a.window_days}日 / 参加者 {len(users)}人")
    for u in users:
        print(f"\n[{u}]")
        for k, v in res[u].items():
            print(f"  {k}: {v}")
    print("\n[全体]")
    print("  7日後利用: ", sum(1 for u in users if res[u]["7日後利用"]), "/", len(users))
    print("  初日3件以上:", sum(1 for u in users if res[u]["初日3件以上"]), "/", len(users))
    print("  通知許可のまま:", sum(1 for u in users if res[u]["通知"] == "許可のまま"), "/", len(users))

if __name__ == "__main__":
    main()
