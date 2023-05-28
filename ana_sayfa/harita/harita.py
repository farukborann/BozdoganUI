from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

class harita(QWidget):
    def __init__(self):
        super().__init__()

        self.loaded = False
        self.layout = QVBoxLayout(self)

        self.browser = QWebEngineView()
        file_path = os.path.join(os.getcwd(), "ana_sayfa/harita/dosyalar/index.html")
        self.browser.load(QUrl.fromLocalFile(file_path))

        self.browser.loadFinished.connect(self.load_finished)

        self.layout.addWidget(self.browser)

    def load_finished(self, ok):
        if ok:
            self.browser.page().runJavaScript("""
                if(true) {
                    let event = new CustomEvent("updateRocket", { detail: ["enlem", "boylam"] });
                    document.dispatchEvent(event);
                }""".replace("enlem", "37.8753143").replace("boylam", "32.4889047"))
            self.browser.page().runJavaScript("""
                if(true) {
                    let event = new CustomEvent("updateFaydaliYuk", { detail: ["enlem", "boylam"] });
                    document.dispatchEvent(event);
                }""".replace("enlem", "37.8753143").replace("boylam", "32.4889047"))
            self.loaded = True

    def update_values(self, veri):
        if(not self.loaded):
            return

        if(veri.sistemno == "3"):
            self.browser.page().runJavaScript("""
                if(true) {
                    let event = new CustomEvent("updateRocket", { detail: ["enlem", "boylam"] });
                    document.dispatchEvent(event);
                }""".replace("enlem", veri.enlem).replace("boylam", veri.boylam))
        if(veri.sistemno == "4"):
            self.browser.page().runJavaScript("""
                if(true) {
                    let event = new CustomEvent("updateFaydaliYuk", { detail: ["enlem", "boylam"] });
                    document.dispatchEvent(event);
                }""".replace("enlem", veri.enlem).replace("boylam", veri.boylam))