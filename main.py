import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget

import qdarktheme

from seri_port.port_ekran import SerialPortWidget
from ana_sayfa.ana_sayfa import MainPageWidget

qdarktheme.enable_hi_dpi()
app = QApplication(sys.argv)
qdarktheme.setup_theme()

window = QMainWindow()
window.setWindowTitle("Bozdoğan Roket Yer İstasyonu V13")
window.setWindowIcon(QIcon("./icons/bozdogan.jfif"))
window.move(0,0)

# Create a tab widget
tab_widget = QTabWidget()

# Set the layout of the first tab to the splitter
ana_sayfa = MainPageWidget()
port_ekran_widget = SerialPortWidget([ana_sayfa.update_values])

second_tab = QWidget()
first_tab = QWidget()

# Second Tab
second_tab_layout = QVBoxLayout()
second_tab_layout.addWidget(ana_sayfa)
second_tab.setLayout(second_tab_layout)

# Set the layout of the first tab to the splitter
first_tab_layout = QVBoxLayout()
first_tab_layout.addWidget(port_ekran_widget)
first_tab.setLayout(first_tab_layout)

tab_widget.addTab(first_tab, "Port Seç")
tab_widget.addTab(second_tab, "Ana Sayfa")

# Set tab widget as central widget
window.setCentralWidget(tab_widget)

# Show the main window
window.showMaximized()

# Run the application
sys.exit(app.exec_())
