from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolBar, QAction,QVBoxLayout
from ana_sayfa.tablolar import tablolar
from ana_sayfa.roket.roket import roket
from ana_sayfa.harita.harita import harita
# from ana_sayfa.grafikler.hizgrafik import hiz
from ana_sayfa.grafikler.grafikler import grafikler
from hyi_paket import hyi_paket

class MainPageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.tablolar = tablolar()
        # self.roket = roket()
        self.harita = harita()
        self.grafikler = grafikler()
        self.hyi_paket = hyi_paket()
      
        self.grid = QGridLayout()
        self.grid.setColumnStretch(0, 0)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 0)
        self.grid.setColumnStretch(1, 1)
      
        self.grid.addWidget(self.tablolar, 0, 0)
        # self.grid.addWidget(self.roket, 0, 1)
        self.grid.addWidget(self.harita, 1, 0)
        self.grid.addWidget(self.grafikler, 1, 1)

        self.setLayout(self.grid)

    def update_values(self, value):
        self.tablolar.update_values(value)
        # self.roket.update_values(value)
        self.harita.update_values(value)
        self.grafikler.update_values(value)
        self.hyi_paket.update_values(value)

