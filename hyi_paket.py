import serial
import struct

class hyi_paket():
    def __init__(self) -> None:
        try:
            self.serial_port = serial.Serial('COM7', 115200, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)
            self.count = 0
        except:
            print("HYI PAKET -> COM_PORT BAGLANTI HATASI !!!")

    # global olarak alınan olusturalacak_paket array'inin check_sum'ini hesaplar.
    def check_sum_hesapla(self, olusturalacak_paket):
        check_sum = sum(olusturalacak_paket[4:75]) % 256
        return check_sum

    def update_values(self, veri):
        if(not hasattr(self, "serial_port")):
            return
        
        # oluşturulan paketin tanımlanması. Kullanım planınıza göre isim ve boyut değişebilir.
        olusturalacak_paket = bytearray(78)
        olusturalacak_paket[0:4] = bytearray([0xFF, 0xFF, 0x54, 0x52])
        olusturalacak_paket[4:6] = bytearray([0x95, self.count])  # Takım ID = 0, Sayac degeri = 0

        if(veri.sistemno =='3'):
            irtifa_float32_uint8_donusturucu = struct.pack('f', float( veri.irtifa))  # Irtifa degerinin atamasini yapıyoruz.
            olusturalacak_paket[6:10] = bytearray(irtifa_float32_uint8_donusturucu)

            roket_gps_irtifa_float32_uint8_donusturucu = struct.pack('f', float( veri.gpsirtifa))  # Roket GPS irtifa
            olusturalacak_paket[10:14] = bytearray(roket_gps_irtifa_float32_uint8_donusturucu)

            roket_enlem_float32_uint8_donusturucu = struct.pack('f', float( veri.enlem))  # Roket GPS irtifa
            olusturalacak_paket[14:18] = bytearray(roket_enlem_float32_uint8_donusturucu)

            roket_boylam_float32_uint8_donusturucu = struct.pack('f', float( veri.boylam))  # Roket GPS irtifa
            olusturalacak_paket[18:22] = bytearray(roket_boylam_float32_uint8_donusturucu)

                
            jiroskopx_float32_uint8_donusturucu = struct.pack('f', float( veri.jiroskopx))  # Roket GPS irtifa
            olusturalacak_paket[46:50] = bytearray(jiroskopx_float32_uint8_donusturucu)

            jiroskopy_float32_uint8_donusturucu = struct.pack('f', float( veri.jiroskopy))  # Roket GPS irtifa
            olusturalacak_paket[50:54] = bytearray(jiroskopy_float32_uint8_donusturucu)

            jiroskopz_float32_uint8_donusturucu = struct.pack('f', float( veri.jiroskopz))  # Roket GPS irtifa
            olusturalacak_paket[54:58] = bytearray(jiroskopz_float32_uint8_donusturucu)

            ivmex_float32_uint8_donusturucu = struct.pack('f', float( veri.ivmex))  # Roket GPS irtifa
            olusturalacak_paket[58:62] = bytearray(ivmex_float32_uint8_donusturucu)

            ivmey_float32_uint8_donusturucu = struct.pack('f', float( veri.ivmey))  # Roket GPS irtifa
            olusturalacak_paket[62:66] = bytearray(ivmey_float32_uint8_donusturucu)

            ivmez_float32_uint8_donusturucu = struct.pack('f', float( veri.ivmez))  # Roket GPS irtifa
            olusturalacak_paket[66:70] = bytearray(ivmez_float32_uint8_donusturucu)
        elif(veri.sistemno =='2'):
            gorevyukugpsirtifa_float32_uint8_donusturucu = struct.pack('f', float( veri.gpsirtifa))  # Roket GPS irtifa
            olusturalacak_paket[22:26] = bytearray(gorevyukugpsirtifa_float32_uint8_donusturucu)

            gorebyukuenlem_float32_uint8_donusturucu = struct.pack('f', float( veri.boylam))  # Roket GPS irtifa
            olusturalacak_paket[26:30] = bytearray(gorebyukuenlem_float32_uint8_donusturucu)

            gorebyukuboylam_float32_uint8_donusturucu = struct.pack('f', float( veri.boylam))  # Roket GPS irtifa
            olusturalacak_paket[30:34] = bytearray(gorebyukuboylam_float32_uint8_donusturucu)

        kademegpsirtifa_float32_uint8_donusturucu = struct.pack('f', 0)  # Roket GPS irtifa
        olusturalacak_paket[34:38] = bytearray(kademegpsirtifa_float32_uint8_donusturucu)

        kademeenlem_float32_uint8_donusturucu = struct.pack('f', 0)  # Roket GPS irtifa
        olusturalacak_paket[38:42] = bytearray(kademeenlem_float32_uint8_donusturucu)

        kademeboylam_float32_uint8_donusturucu = struct.pack('f', 0)  # Roket GPS irtifa
        olusturalacak_paket[42:46] = bytearray(kademeboylam_float32_uint8_donusturucu)

        aci_float32_uint8_donusturucu = struct.pack('f', 5.5)  # Roket GPS irtifa
        olusturalacak_paket[70:74] = bytearray(aci_float32_uint8_donusturucu)

        check_sum = self.check_sum_hesapla(olusturalacak_paket)
        olusturalacak_paket[75] = check_sum
        olusturalacak_paket[76:78] = bytearray([0x0D, 0x0A])

        self.serial_port.write(olusturalacak_paket)
        self.count += 1
        print("HYI PAKET -> PAKET GÖNDERİLDİ")