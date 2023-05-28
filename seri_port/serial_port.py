import serial.tools.list_ports

from veri import veri

class serial_port():
    def __init__(self, selected_port, baudrate, simulate=False):
        self.simulate = simulate # Simüle et
        if(simulate):
            self.sim_veri = veri(["0","3","2","3","4","5","6","7","8","9","10","11","37.8726666","32.491876","14","15","16","17","18","19","20","21"])
            print("SP -> PORT AÇILDI (Simülasyon)")
            return
        
        self.serial_port = serial.Serial(selected_port, baudrate=baudrate)
        print("SP -> PORT AÇILDI")

    def paket_bol(self, veri):
        veriler = []

        dik_veriler = veri.split("|")
        for veri in dik_veriler:
            r_veriler = veri.split("\r")
            for _veri in r_veriler:
                if(_veri.strip() == ""):
                    continue
                
                values = _veri.split("*")
                if(len(values) > 22):
                    if(int(values[0]) + 1 == int(values[22])):
                        veriler.append(values[0: 22])
                        veriler.append(values[21: 44])
                    else:
                        print("WE FUCKED") # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                elif(len(values) == 22):
                    veriler.append(values)
                else:
                    print("SP -> BOZUK VERİ !!! -> Uzunluk : ", len(values))

        return veriler

    def veri_oku(self):
        if(self.simulate):
            self.sim_veri.paketno = str(int(self.sim_veri.paketno) + 1)

            self.sim_veri.enlem = str(float(self.sim_veri.enlem) + 0.0001)
            self.sim_veri.boylam = str(float(self.sim_veri.boylam) + 0.0001)
            self.sim_veri.gpsirtifa = str(float(self.sim_veri.gpsirtifa) + 1)

            self.sim_veri.ivmex = str(float(self.sim_veri.ivmex) + 1)
            self.sim_veri.ivmey = str(float(self.sim_veri.ivmey) + 1)
            self.sim_veri.ivmez = str(float(self.sim_veri.ivmez) + 1)

            self.sim_veri.jiroskopx = str(float(self.sim_veri.jiroskopx) + 1)
            self.sim_veri.jiroskopy = str(float(self.sim_veri.jiroskopy) + 1)
            self.sim_veri.jiroskopz = str(float(self.sim_veri.jiroskopz) + 1)

            print("SP -> VERİ OKUNDU")
            return [self.sim_veri]
        
        if(self.serial_port == None):
            return None

        try:
            if self.serial_port and self.serial_port.is_open and self.serial_port.in_waiting:
                raw_data = self.serial_port.readline()
                raw_data = raw_data.decode('utf')

                raw_veriler = self.paket_bol(raw_data)

                if(len(raw_veriler) < 1):
                    print("SP -> BOZUK VERİ !!!")
                    return None
                
                veriler = []
                for _veri in raw_veriler:
                    veriler.append(veri(_veri))

                print("SP -> VERİ OKUNDU")
                return veriler
            else:
                print("SP -> BEKLEYEN VERİ YOK")
                return []
        except Exception as ex:
            print(ex)
            print("SP -> VERİ OKUNAMADI !!!")

        return None


    def port_kapat(self):
        if(self.simulate == False):
            self.serial_port.close()
            
        print("SP -> PORT KAPATILDI")

    @staticmethod
    def acik_portlar():
        return serial.tools.list_ports.comports()
