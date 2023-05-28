from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame, QLineEdit, QGridLayout

class tablolar(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)

        # Horizontal layout for the three widgets
        self.layout = QHBoxLayout()
        self.layout.setSpacing(10)  #birbirinden ayırıyor

        self.widget1 = self.create_sistem_widget("Birinci Sistem:")   #widget isimleri
        self.widget2 = self.create_sistem_widget("İkinci Sistem:")
        self.widget3 = self.create_sistem_widget("Görev Yükü:")

        # self.widget1.setStyleSheet("background-color: #FFEFD5")
        # self.widget2.setStyleSheet("background-color: #FFEFD5")
        # self.widget3.setStyleSheet("background-color: #FFEFD5")

        self.layout.addWidget(self.widget1)   #widget numaraları
        self.layout.addWidget(self.widget2)
        self.layout.addWidget(self.widget3)

        self.setLayout(self.layout)

    def create_sistem_widget(self, sistem_adi):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)
        layout = QGridLayout(frame)

        label = QLabel(sistem_adi)
        label.setStyleSheet("font-weight: bold" ) #yazı tipini değiştiriyor
        label.setMaximumHeight(25)
        layout.addWidget(label) # widgetlerin içindekilerinin konumunu değiştiriyor

        ana_paket = QLineEdit()
        ana_paket.setReadOnly(True)  #değer girmemize izin veriyor
        ana_paket.setObjectName("paket")
        layout.addWidget(QLabel("Paket:"), 1, 0) #konum değiştiriyor
        layout.addWidget(ana_paket, 1, 1)

        ana_takim_id = QLineEdit()
        ana_takim_id.setReadOnly(True)
        ana_takim_id.setObjectName("takimid")
        layout.addWidget(QLabel("Takım ID:"), 2, 0)
        layout.addWidget(ana_takim_id, 2, 1)

        ana_irtifa = QLineEdit()
        ana_irtifa.setReadOnly(True)
        ana_irtifa.setObjectName("irtifa")
        layout.addWidget(QLabel("İrtifa:"), 3, 0)
        layout.addWidget(ana_irtifa, 3, 1)

        ana_ivme = QLineEdit()
        ana_ivme.setReadOnly(True)
        ana_ivme.setObjectName("ivme")
        layout.addWidget(QLabel("İvme:"), 4, 0)
        layout.addWidget(ana_ivme, 4, 1)

        ana_eğim = QLineEdit()
        ana_eğim.setReadOnly(True)
        ana_eğim.setObjectName("eğim")
        layout.addWidget(QLabel("Eğim:"), 5, 0)
        layout.addWidget(ana_eğim, 5, 1)

        ana_enlem = QLineEdit()
        ana_enlem.setReadOnly(True)
        ana_enlem.setObjectName("enlem")
        layout.addWidget(QLabel("Enlem:"), 6, 0)
        layout.addWidget(ana_enlem, 6, 1)

        ana_boylam = QLineEdit()
        ana_boylam.setReadOnly(True)
        ana_boylam.setObjectName("boylam")
        layout.addWidget(QLabel("Boylam:"), 7, 0)
        layout.addWidget(ana_boylam, 7, 1)


        ana_sicaklik = QLineEdit()
        ana_sicaklik.setReadOnly(True)
        ana_sicaklik.setObjectName("sicaklik")
        layout.addWidget(QLabel("Sıcaklık:"), 8, 0)
        layout.addWidget(ana_sicaklik, 8, 1)

        ana_nem = QLineEdit()
        ana_nem.setReadOnly(True)
        ana_nem.setObjectName("nem")
        layout.addWidget(QLabel("Nem:"), 9, 0)
        layout.addWidget(ana_nem, 9, 1)

        ana_atesleme_durumu = QLineEdit()
        ana_atesleme_durumu.setReadOnly(True)
        ana_atesleme_durumu.setObjectName("ateslemedurumu")
        layout.addWidget(QLabel("Ateşleme Durumu:"), 10, 0)
        layout.addWidget(ana_atesleme_durumu, 10, 1)

        frame.setLayout(layout)

        return frame

    def update_values(self, veri):
        # # Update the values in the UI
        widget = None
        if(veri.sistemno=='3'):
            widget = self.widget1
        elif(veri.sistemno=='2'):
            widget = self.widget2
        elif(veri.sistemno=='4'):
            widget = self.widget3

        widget.findChild(QLineEdit, "paket").setText(str(veri.paketno))
        widget.findChild(QLineEdit, "ivme").setText(str(veri.ivmex))
        widget.findChild(QLineEdit, "irtifa").setText(str(veri.irtifa))
        widget.findChild(QLineEdit, "sicaklik").setText(str(veri.sicaklik))
        widget.findChild(QLineEdit, "nem").setText(str(veri.nem))
        widget.findChild(QLineEdit, "eğim").setText(str(veri.jiroskopx))
        widget.findChild(QLineEdit, "enlem").setText(str(veri.enlem))
        widget.findChild(QLineEdit, "boylam").setText(str(veri.boylam))
        widget.findChild(QLineEdit, "takimid").setText(str(veri.takimid))
        widget.findChild(QLineEdit, "ateslemedurumu").setText(str(veri.parasutdurum))