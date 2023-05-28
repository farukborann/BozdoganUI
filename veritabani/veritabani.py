import sqlite3

class veri_tabani():
    def __init__(self):
        self.connection = sqlite3.connect("./veritabani/veriler.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def veri_ekle(self, veri):
        _veri = (veri.takimid, veri.sistemno, veri.paketno, veri.irtifa, veri.ivmex, veri.ivmey, veri.ivmez,
                    veri.jiroskopx, veri.jiroskopy, veri.jiroskopz,
                    veri.sicaklik, veri.nem, veri.enlem, veri.boylam, veri.gpsirtifa, veri.parasutdurum, veri.roketsaat,
                    veri.roketdakika, veri.roketsaniye,
                    veri.pilsicaklik, veri.pilyuzdesi, veri.uydusayisi)

        dbname = ""
        if (veri.sistemno == '3'):
            dbname = "ANASISTEMVERITABANI"
        elif(veri.sistemno == '2'):
            dbname = "YEDEKSISTEMVERITABANI"
        elif(veri.sistemno == '4'):
            dbname = "FAYDALIYUKVERITABANI"

        # for _veri in veriler:
        self.connection.execute(
            'INSERT INTO '
            + dbname +
            ' (takimid,sistemno,paketno,irtifa,ivmex,ivmey,ivmez,jiroskopx,jiroskopy,jiroskopz,sicaklik,nem,enlem,boylam,gpsirtifa,parasutdurum,saat,dakika,saniye,pilsicaklik,pilyuzdesi,uydusayisi) '
            ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            _veri)
        
        self.connection.commit()

        print("DB -> VERİ EKLENDİ (?)") 