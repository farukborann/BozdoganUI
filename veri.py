takim_id = ""

class veri():
    def __init__(self, data):
        global takim_id
        self.paketno = data[0]
        self.sistemno = data[1]
        self.takimid = takim_id
        self.irtifa = data[3]
        self.ivmex = data[4]
        self.ivmey = data[5]
        self.ivmez = data[6]
        self.jiroskopx = data[7]
        self.jiroskopy = data[8]
        self.jiroskopz = data[9]
        self.sicaklik = data[10]
        self.nem = data[11]
        self.enlem = data[12]
        self.boylam = data[13]
        self.gpsirtifa = data[14]
        self.parasutdurum = data[15]
        self.roketsaat = data[16]
        self.roketdakika = data[17]
        self.roketsaniye = data[18]
        self.pilsicaklik = data[19]
        self.pilyuzdesi = data[20]
        self.uydusayisi=data[21]
    
    def __str__(self) -> str:
        return "{0}*{1}*{2}*{3}*{4}*{5}*{6}*{7}*{8}*{9}*{10}*{11}*{12}*{13}*{14}*{15}*{16}*{17}*{18}*{19}*{20}*{21}|".format(self.paketno, self.sistemno,
                                                                                                                             self.takimid, self.irtifa,
                                                                                                                             self.ivmex, self.ivmey, self.ivmez,
                                                                                                                             self.jiroskopx, self.jiroskopy, self.jiroskopz,
                                                                                                                             self.sicaklik, self.nem,
                                                                                                                             self.enlem, self.boylam, self.gpsirtifa,
                                                                                                                             self.parasutdurum, 
                                                                                                                             self.roketsaat, self.roketdakika, self.roketsaniye,
                                                                                                                             self.pilsicaklik, self.pilyuzdesi,
                                                                                                                             self.uydusayisi)