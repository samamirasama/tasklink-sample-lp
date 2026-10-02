// 検証用スパイク（未コンパイル）。共有コンテナへの保存と読み出し。両ターゲットに追加する。
import Foundation

let appGroupID = "group.jp.example.atospike" // ← 手順3の識別子に合わせる

struct CapturedItem: Codable, Identifiable {
    var id: String = UUID().uuidString
    var capturedAt: Date = Date()
    var sourceApp: String?            // 取得できれば共有元のバンドルIDなど（通常は取れない。推測で埋めない）
    var typeIdentifiers: [String]     // NSItemProvider.registeredTypeIdentifiers の生の一覧
    var urlString: String?            // public.url の値
    var urlCameAs: String?            // "URL" / "Data" / "String" / nil（受け取り型の記録）
    var text: String?                 // public.plain-text / attributedContentText
    var imageFileNames: [String] = [] // 共有コンテナに保存した画像ファイル名
    var elapsedMs: Int = 0            // 受信開始から保存完了までのミリ秒
    var note: String?                 // エラーや警告
}

enum SharedStore {
    static var containerURL: URL {
        FileManager.default.containerURL(forSecurityApplicationGroupIdentifier: appGroupID)!
    }
    static var itemsDir: URL { containerURL.appendingPathComponent("items", isDirectory: true) }
    static var imagesDir: URL { containerURL.appendingPathComponent("images", isDirectory: true) }

    static func prepare() {
        for d in [itemsDir, imagesDir] {
            try? FileManager.default.createDirectory(at: d, withIntermediateDirectories: true)
        }
    }

    // 1件を JSON ファイルとして保存（拡張側）。書き込みは原子的に行う。
    static func save(_ item: CapturedItem) throws {
        prepare()
        let data = try JSONEncoder().encode(item)
        try data.write(to: itemsDir.appendingPathComponent("\(item.id).json"), options: .atomic)
    }

    static func saveImage(_ data: Data, ext: String) throws -> String {
        prepare()
        let name = "\(UUID().uuidString).\(ext)"
        try data.write(to: imagesDir.appendingPathComponent(name), options: .atomic)
        return name
    }

    // 全件読み出し（本体側）。新しい順。
    static func loadAll() -> [CapturedItem] {
        prepare()
        let files = (try? FileManager.default.contentsOfDirectory(at: itemsDir, includingPropertiesForKeys: nil)) ?? []
        return files.compactMap { url in
            guard let d = try? Data(contentsOf: url) else { return nil }
            return try? JSONDecoder().decode(CapturedItem.self, from: d)
        }.sorted { $0.capturedAt > $1.capturedAt }
    }
}
