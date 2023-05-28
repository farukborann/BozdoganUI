from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QHBoxLayout
from ana_sayfa.grafikler.ivme import ivme
from ana_sayfa.grafikler.alinan_yol import alinan_yol
from ana_sayfa.grafikler.hiz import hiz

class grafikler(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget()
        self.layout = QHBoxLayout()
        self.layout.setSpacing(10)  #birbirinden ayırıyor

        # Set the layout of the first tab to the splitter
        self.ivme_widget = ivme()
        self.alinan_yol_widget = alinan_yol()
        self.hiz_widget = hiz()

        self.ivme_tab = QWidget()
        ivme_tab_layout = QVBoxLayout()
        ivme_tab_layout.addWidget(self.ivme_widget)
        self.ivme_tab.setLayout(ivme_tab_layout)

        self.alinan_yol_tab = QWidget()
        alinan_yol_tab_layout = QVBoxLayout()
        alinan_yol_tab_layout.addWidget(self.alinan_yol_widget)
        self.alinan_yol_tab.setLayout(alinan_yol_tab_layout)

        self.hiz_tab = QWidget()
        hiz_tab_layout = QVBoxLayout()
        hiz_tab_layout.addWidget(self.hiz_widget)
        self.hiz_tab.setLayout(hiz_tab_layout)

        self.tab_widget.addTab(self.ivme_tab, "Ivme")
        self.tab_widget.addTab(self.alinan_yol_tab, "Alinan Yol")
        self.tab_widget.addTab(self.hiz_tab, "Hiz")

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def update_values(self, value):
        self.ivme_widget.update_values(value)
        self.alinan_yol_widget.update_values(value)
        self.hiz_widget.update_values(value)
