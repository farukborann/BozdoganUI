import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtCore import QTimer
import threading

from veritabani.veritabani import veri_tabani
from seri_port.serial_port import serial_port
import veri

class SerialPortWidget(QWidget):
    def __init__(self, tick_funcs):
        super().__init__()
        self.tick_funcs = tick_funcs
        
        # Arayüz öğeleri
        self.port_list_label = QLabel('Açık Portlar:')
        self.port_list_widget = QComboBox()
        self.baudrate_label = QLabel('Baudrate:')
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItem('9600')
        self.baudrate_combo.addItem('19200')
        self.baudrate_combo.addItem('38400')
        self.baudrate_combo.addItem('57600')
        self.baudrate_combo.addItem('74880')
        self.baudrate_combo.addItem('115200')
        self.refresh_button = QPushButton('Yenile')
        self.connect_button = QPushButton('Bağlan')
        self.disconnect_button = QPushButton('Bağlantıyı Kes')
        self.data_label = QLabel('Alınan Veri:')
        self.status_label = QLabel()
        self.takım_id_label = QLabel('Takım ID:')
        self.takım_id_line_edit = QLineEdit()
        self.set_team_id_button = QPushButton('Uygula')

        # Arayüz düzeni
        layout = QVBoxLayout()

        port_layout = QHBoxLayout()
        port_layout.addWidget(self.port_list_label)
        port_layout.addWidget(self.port_list_widget)
        layout.addLayout(port_layout)

        baud_layout = QHBoxLayout()
        baud_layout.addWidget(self.baudrate_label)
        baud_layout.addWidget(self.baudrate_combo)
        layout.addLayout(baud_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.disconnect_button)
        layout.addLayout(button_layout)

        takim_id_layout = QHBoxLayout()
        takim_id_layout.setContentsMargins(0,100,0,0)
        takim_id_button_layout = QHBoxLayout()

        takim_id_layout.addWidget(self.takım_id_label)
        takim_id_layout.addWidget(self.takım_id_line_edit)
        takim_id_button_layout.addWidget(self.set_team_id_button)
        layout.addLayout(takim_id_layout)
        layout.addLayout(takim_id_button_layout)

        data_label_layout = QHBoxLayout()
        data_label_layout.addWidget(self.data_label)
        layout.addLayout(data_label_layout)

        status_label_layout = QHBoxLayout()
        status_label_layout.addWidget(self.status_label)
        layout.addLayout(status_label_layout)

        self.setLayout(layout)

        # Olayları bağlama
        self.refresh_button.clicked.connect(self.refresh_ports)
        self.refresh_button.setStyleSheet("border-radius: 10px; background-color: #00BFFF; color: black;")
        self.connect_button.clicked.connect(self.connect_port)
        self.disconnect_button.clicked.connect(self.close_port)
        self.set_team_id_button.clicked.connect(self.set_team_id)

        # Açık portları listeleme
        self.refresh_ports()

        self.veri_tabani = veri_tabani()

        self.timer = QTimer()
        self.timer.timeout.connect(self.arayuz_guncelle)
        self.timer.start(75)


    def arayuz_kilit(self):
        if(hasattr(self, "serial_port")):
            self.disconnect_button.setEnabled(True)
            self.connect_button.setEnabled(False)
            self.connect_button.setStyleSheet("border-radius: 10px; background-color: #dddddd; color: black;")
            self.disconnect_button.setStyleSheet("border-radius: 10px; background-color: #00BFFF; color: black;")
        else:
            self.disconnect_button.setEnabled(False)
            self.connect_button.setEnabled(True)
            self.disconnect_button.setStyleSheet("border-radius: 10px; background-color: #dddddd; color: black;")
            self.connect_button.setStyleSheet("border-radius: 10px; background-color: #00BFFF; color: black;")

    def serial_port_guncelle(self):
        if hasattr(self, "serial_port"):
            veri = self.serial_port.veri_oku()

            if(veri == None):
                print("UI -> BOZUK VERİ")
                return
            elif(len(veri) == 0):
                return

            for _veri in veri:
                self.veri_tabani.veri_ekle(_veri)
            
            for func in self.tick_funcs:
                thread = threading.Thread(target=func, args=[veri[-1]])
                thread.start()

    def arayuz_guncelle(self):
        thread = threading.Thread(target=self.serial_port_guncelle)
        thread.start()

    def refresh_ports(self):
        self.port_list_widget.clear()
        ports = serial_port.acik_portlar()
        for info in ports:
            self.port_list_widget.addItem(info.device)
        
        self.status_label.setText('Portlar Yenilendi')
        self.arayuz_kilit()

    def connect_port(self):
        try:
            selected_port = self.port_list_widget.currentText()
            baudrate = int(self.baudrate_combo.currentText())
            self.serial_port = serial_port(selected_port, baudrate, True)
            self.status_label.setText('Baglanildi => ' + selected_port)
        except:
            self.status_label.setText('Baglanmada Hata')
        
        self.arayuz_kilit()

    def close_port(self):
        self.serial_port.port_kapat()
        delattr(self, "serial_port")
        self.status_label.setText('Bağlantı Kapatıldı')
        self.arayuz_kilit()

    def set_team_id(self):
        veri.takim_id = self.takım_id_line_edit.text()
        self.status_label.setText('Takim ID Ayarlandi')
        print("Takim ID Ayarlandi")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SerialPortWidget()
    widget.show()
    sys.exit(app.exec_())