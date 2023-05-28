import numpy as np
import datetime
import collections
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class alinan_yol(QWidget):
    def __init__(self):
        super().__init__()

        self.grafik_uzunluk = 200
        self.tick_count = 1
        self.toplam_yol = 0

        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout.addWidget(self.toolbar)

        self.plot_area = self.canvas.figure.add_subplot()

        self.ana_sistem_x = []
        self.ana_sistem_y = collections.deque(maxlen=self.grafik_uzunluk)
        self.ana_sistem_line, = self.plot_area.plot(self.ana_sistem_x, self.ana_sistem_y, color="green", label="ana sistem ivme")

        self.yedek_sistem_x = []
        self.yedek_sistem_y = collections.deque(maxlen=self.grafik_uzunluk)
        self.yedek_sistem_line, = self.plot_area.plot(self.yedek_sistem_x, self.yedek_sistem_y, color="gray", label="yedek sistem ivme")

        self.faydali_yuk_x = []
        self.faydali_yuk_y = collections.deque(maxlen=self.grafik_uzunluk)
        self.faydali_yuk_line, = self.plot_area.plot(self.faydali_yuk_x, self.faydali_yuk_y, color="red", label="faydali yuk ivme")

        self.plot_area.legend(loc="upper left")


    def update_values(self, veri):
        line = None
        x = None
        y = None

        if(veri.sistemno == "3"):
            line = self.ana_sistem_line
            x = self.ana_sistem_x
            y = self.ana_sistem_y
        elif(veri.sistemno == "2"):
            line = self.yedek_sistem_line
            x = self.yedek_sistem_x
            y = self.yedek_sistem_y
        elif(veri.sistemno == "4"):
            line = self.ana_sistem_line
            x = self.ana_sistem_x
            y = self.ana_sistem_y
        

        x.append(datetime.datetime.now())

        yeni_ivme = np.sqrt(float(veri.ivmex)** 2 + float(veri.ivmey) ** 2 + float(veri.ivmez) ** 2)
        hiz = yeni_ivme * self.tick_count
        alinan_yol = hiz * self.tick_count

        self.toplam_yol += alinan_yol
        self.tick_count += 1

        y.append(self.toplam_yol)

        # Grafikleri yeniden çiz
        line.set_data(x[-self.grafik_uzunluk:], y)

        self.plot_area.relim()
        self.plot_area.autoscale_view()
        self.plot_area.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M:%S'))
        self.canvas.draw()
