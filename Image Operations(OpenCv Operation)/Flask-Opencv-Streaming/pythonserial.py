import serial
import time

def pythonSerial():
    # burada portumuzu okuyoruz...
    port = serial.Serial("COM7"  # com girilmesi gerekli
                         , baudrate=9600  # baund rate
                         , timeout=0)  # zaman aşım

    #port_okunan = port.readline()[:-2]  # readline ile veriyi okuyup barçalıyoruz
    #print("Mpu dan okunan X derecesi : {}".format(port_okunan.decode("ascii")))  # format ile ekrana veriyi bastıroyruz aynı zamanda ise
    # decode diyerek parçalama işlemi yapıyoruz...

    hız = int(input("hız giriniz "))

    while True:
        #hız2=int(input("Hız ne olsun 30 için 2"))


        port.write(hız)

        print(hız)

        if 0xFF==ord("q"):
            print("cıkıs yapılıyor")
            break

    #return port_okunan.decode("ascii")

if __name__=="__main__":
    pythonSerial()
