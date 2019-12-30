import cv2
import  numpy as np

kamera=cv2.VideoCapture("video.mp4")

resim=cv2.imread('resim.jpg',0)

while True:
    ret,kare=kamera.read()

    w,h=resim.shape#(genislik,yukselik)

    gri_kare=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    #ozel bir fonksiyon
    #gri_kare ile resmi karşılaştırıyor
    #0 ile 1 arasında bir değer veriyor
    res=cv2.matchTemplate(gri_kare,resim,cv2.TM_CCOEFF_NORMED)
    #eşik değer ise biz kaçtan büyük oldugnu ayarlıyoruz
    esik_Degeri=0.73

    loc=np.where(res>esik_Degeri)
    print(loc)
    #(array([], dtype=int32), array([], dtype=int32))
    # loc cıkısı
    # zip fonksiyonu ile parçalama ilemi yapıyoruz
    for i in zip(*loc[::-1]):
        cv2.rectangle(kare,#kareye belirlenen değerleri gir
                      i,# P1 dir
                      (i[0]+h,#karenin yüklesiğni ayarala P2 dir
                       i[1]+w),#karenin genişliğini ayarla
                      (0,255,0),#karenin rengini ayarla
                      1)# karenin kalıngını belirle
        cv2.putText(kare,'A',(i[0]+50,i[1]+50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

    cv2.imshow('Kare',kare)
    cv2.imshow('Gri Kare',gri_kare)
    cv2.imshow('Resim',resim)

    #cv2.imshow('Gri Resim',gri_resim)
    if cv2.waitKey(50)&0xFF==ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()