// 検証用スパイク（未コンパイル）。共有拡張：受け取った内容を記録して即保存し、閉じる。
// 方針：拡張内では通信・解析をしない。受信 → 共有コンテナに保存 → completeRequest。
import UIKit
import UniformTypeIdentifiers
import UserNotifications

final class ShareViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        let label = UILabel()
        label.text = "保存中…"
        label.textAlignment = .center
        label.frame = view.bounds
        label.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(label)
        Task { await capture(); self.extensionContext?.completeRequest(returningItems: nil) }
    }

    private func capture() async {
        let start = Date()
        var item = CapturedItem(typeIdentifiers: [])
        guard let inputItems = extensionContext?.inputItems as? [NSExtensionItem] else {
            item.note = "inputItems なし"; try? SharedStore.save(item); return
        }
        for input in inputItems {
            if let attributed = input.attributedContentText?.string, !attributed.isEmpty {
                item.text = (item.text ?? "") + attributed
            }
            for provider in input.attachments ?? [] {
                item.typeIdentifiers.append(contentsOf: provider.registeredTypeIdentifiers)

                // URL：URL型・Data型・String型のどれで来るかを記録する
                if provider.hasItemConformingToTypeIdentifier(UTType.url.identifier) {
                    if let raw = try? await provider.loadItem(forTypeIdentifier: UTType.url.identifier) {
                        switch raw {
                        case let u as URL: item.urlString = u.absoluteString; item.urlCameAs = "URL"
                        case let d as Data: item.urlString = String(data: d, encoding: .utf8); item.urlCameAs = "Data"
                        case let s as String: item.urlString = s; item.urlCameAs = "String"
                        default: item.urlCameAs = String(describing: type(of: raw))
                        }
                    }
                }
                // テキスト
                if provider.hasItemConformingToTypeIdentifier(UTType.plainText.identifier) {
                    if let raw = try? await provider.loadItem(forTypeIdentifier: UTType.plainText.identifier) {
                        if let s = raw as? String { item.text = (item.text ?? "") + s }
                        else if let d = raw as? Data, let s = String(data: d, encoding: .utf8) { item.text = (item.text ?? "") + s }
                    }
                }
                // 画像：拡張のメモリ上限を考え、Data のまま書き出す（デコードしない）
                if provider.hasItemConformingToTypeIdentifier(UTType.image.identifier) {
                    if let raw = try? await provider.loadItem(forTypeIdentifier: UTType.image.identifier) {
                        var data: Data?
                        var ext = "img"
                        if let u = raw as? URL { data = try? Data(contentsOf: u); ext = u.pathExtension.isEmpty ? "img" : u.pathExtension }
                        else if let d = raw as? Data { data = d }
                        else if let img = raw as? UIImage { data = img.jpegData(compressionQuality: 0.8); ext = "jpg" }
                        if let data, let name = try? SharedStore.saveImage(data, ext: ext) { item.imageFileNames.append(name) }
                        else { item.note = (item.note ?? "") + "画像保存失敗; " }
                    }
                }
            }
        }
        item.elapsedMs = Int(Date().timeIntervalSince(start) * 1000)
        do { try SharedStore.save(item) } catch { item.note = "保存失敗: \(error)" }

        // 試験E-1：本体へ誘導するローカル通知（権限は本体で取得済みであること）
        let content = UNMutableNotificationContent()
        content.title = "保存しました"
        content.body = "AtoSpike を開いて内容を確認できます"
        let req = UNNotificationRequest(identifier: item.id, content: content, trigger: nil)
        try? await UNUserNotificationCenter.current().add(req)
    }
}
