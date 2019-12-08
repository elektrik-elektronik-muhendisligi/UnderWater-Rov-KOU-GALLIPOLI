import cv2
import numpy as np
import serial

''' Buradan aşağıdakiler bizim projemiz de ki modlar'''
from display_stabilazator import display_stabilazatora
import pythonserial

kamera=cv2.VideoCapture(0)

# burada portumuzu okuyoruz...
port = serial.Serial("COM4"  # com girilmesi gerekli
                         , baudrate=9600  # baund rate
                         , timeout=0)  # zaman aşım
def main():

    while(True):

        #port=pythonserial.pythonSerial()

        port_okunan = port.readline()[:-2]  # readline ile veriyi okuyup barçalıyoruz
        print("Mpu dan okunan X derecesi : {}".format(
            port_okunan.decode("ascii")))  # format ile ekrana veriyi bastıroyruz aynı zamanda ise
        # decode diyerek parçalama işlemi yapıyoruz...

        #print(port)


        '''ret kamera bilgisinin çalısıp çalısmadıgını kontrol ederken kare ise kameradan alınan bilgileri ekrana bastıryoruz...'''
        ret,kare=kamera.read()

        resim = display_stabilazatora.DisplayStabilzator(kare)

        cv2.imshow('Mpu060 Ekran Dengeliyici',resim)

        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
