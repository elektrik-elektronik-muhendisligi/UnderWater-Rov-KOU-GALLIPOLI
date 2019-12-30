import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)#BOARD da olabilir
GPIO.setup(18,GPIO.OUT)#çýkýþ olarak tanimla

pwm=GPIO.PWM(18,50)#18. GPIO pinine 50Hz olacak bir biçimde
#pulse bilgisi gitsin

def acilama(aci): # aci degerine çeviri
    return ((float(aci)/18.0) + 2)

pwm.start(acilama(0))#baslangic acisi belirleme

for i in range(0,181,45): #sifirdan +45 lik 180 e kadar art
    print (i,"derece")
    pwm.ChangeDutyCycle(acilama(i))#return edilen bilgiyi
    #pwm bilgi olarak 18. pine yönlendir
    time.sleep(1)

pwm.stop()#haberlesmeyi keser
GPIO.cleanup()#GPIO pinleri hafizasinda ki bilgileri temizler

