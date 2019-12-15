import serial

def pythonSerial():
    # burada portumuzu okuyoruz...
    port = serial.Serial("COM4"  # com girilmesi gerekli
                         , baudrate=9600  # baund rate
                         , timeout=0)  # zaman aşım

    port_okunan = port.readline()[:-2]  # readline ile veriyi okuyup barçalıyoruz
    print("Mpu dan okunan X derecesi : {}".format(
        port_okunan.decode("ascii")))  # format ile ekrana veriyi bastıroyruz aynı zamanda ise
    # decode diyerek parçalama işlemi yapıyoruz...

    return port_okunan.decode("ascii")

if __name__=="__main__":
    pythonSerial()
