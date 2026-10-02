// 検証用スパイク（未コンパイル）。本体：記録の一覧、メタデータ取得、OCR、端末内LLM可用性。
import SwiftUI
import LinkPresentation
import Vision
import UserNotifications
#if canImport(FoundationModels)
import FoundationModels
#endif

struct ContentView: View {
    @State private var items: [CapturedItem] = []
    @State private var log: [String] = []

    var body: some View {
        NavigationStack {
            List {
                Section("操作") {
                    Button("通知権限を要求") { Task { _ = try? await UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound]) } }
                    Button("LLM可用性（Foundation Models）") { checkLLM() }
                    Button("OCR対応言語") { ocrLanguages() }
                    Button("再読み込み") { items = SharedStore.loadAll() }
                }
                Section("記録（\(items.count)件）") {
                    ForEach(items) { it in
                        VStack(alignment: .leading, spacing: 4) {
                            Text(it.capturedAt.formatted()).font(.caption)
                            Text("型: " + it.typeIdentifiers.joined(separator: ", ")).font(.caption2)
                            if let u = it.urlString { Text("URL(\(it.urlCameAs ?? "?")): \(u)").font(.caption) }
                            if let t = it.text { Text("text: \(t.prefix(120))").font(.caption) }
                            Text("画像\(it.imageFileNames.count)枚 / \(it.elapsedMs)ms \(it.note ?? "")").font(.caption2)
                            HStack {
                                if let u = it.urlString.flatMap(URL.init) { Button("メタデータ取得") { fetchMetadata(u) } }
                                if let name = it.imageFileNames.first { Button("OCR") { ocr(name) } }
                            }.buttonStyle(.bordered)
                        }
                    }
                }
                Section("ログ") { ForEach(log.indices, id: \.self) { Text(log[$0]).font(.caption2) } }
            }
            .navigationTitle("AtoSpike")
            .onAppear { items = SharedStore.loadAll() }
        }
    }

    // 試験B：LinkPresentation。ログイン必須ページの挙動を見る。
    func fetchMetadata(_ url: URL) {
        let start = Date()
        let provider = LPMetadataProvider()
        provider.timeout = 15
        provider.startFetchingMetadata(for: url) { meta, error in
            let ms = Int(Date().timeIntervalSince(start) * 1000)
            DispatchQueue.main.async {
                if let error { log.append("META ✗ \(ms)ms \(url.host ?? "") \(error.localizedDescription)") }
                else { log.append("META ✓ \(ms)ms title=\(meta?.title ?? "nil") image=\(meta?.imageProvider != nil)") }
            }
        }
    }

    // 試験C：Vision。対応言語に ja が含まれるか。
    func ocrLanguages() {
        if #available(iOS 18.0, *) {
            Task {
                let req = RecognizeTextRequest()
                let langs = (try? req.supportedRecognitionLanguages.map { $0.identifier }) ?? []
                await MainActor.run { log.append("OCR langs: \(langs.joined(separator: ","))") }
            }
        } else {
            let req = VNRecognizeTextRequest()
            let langs = (try? req.supportedRecognitionLanguages()) ?? []
            log.append("OCR langs(legacy): \(langs.joined(separator: ","))")
        }
    }

    func ocr(_ fileName: String) {
        let url = SharedStore.imagesDir.appendingPathComponent(fileName)
        guard let data = try? Data(contentsOf: url), let cg = UIImage(data: data)?.cgImage else { log.append("OCR: 画像読込失敗"); return }
        let req = VNRecognizeTextRequest { r, e in
            let texts = (r.results as? [VNRecognizedTextObservation])?.compactMap { $0.topCandidates(1).first?.string } ?? []
            DispatchQueue.main.async { log.append("OCR: \(texts.joined(separator: " / ").prefix(300)) \(e.map { "err=\($0)" } ?? "")") }
        }
        req.recognitionLevel = .accurate
        req.recognitionLanguages = ["ja", "en"]
        try? VNImageRequestHandler(cgImage: cg).perform([req])
    }

    // 試験D：Foundation Models の可用性と日本語タグ付け。
    func checkLLM() {
        #if canImport(FoundationModels)
        if #available(iOS 26.0, *) {
            let model = SystemLanguageModel(useCase: .contentTagging)
            switch model.availability {
            case .available:
                log.append("LLM: available, supportsJa=\(model.supportsLocale(Locale(identifier: "ja_JP")))")
                Task {
                    let session = LanguageModelSession(model: model)
                    let sample = items.first?.text ?? "渋谷の新しいカフェ、週末に行きたい。限定のプリンが有名らしい。"
                    do {
                        let r = try await session.respond(to: "次の文に、行く／買う／やる／見る／覚えておく のいずれかの行動タグを付けて: \(sample)")
                        await MainActor.run { log.append("LLM tag: \(r.content)") }
                    } catch { await MainActor.run { log.append("LLM err: \(error)") } }
                }
            case .unavailable(let reason):
                log.append("LLM: unavailable \(reason)")
            }
        } else { log.append("LLM: iOS 26 未満") }
        #else
        log.append("LLM: FoundationModels を import できない SDK")
        #endif
    }
}
