import cv2
import numpy as np

b=255 #fonksiyonlarda ki blue kodu
g=255 #fonk* green kodu
r=255 #fonk* red kodu

def DisplayStabilzator(resim):

    'asagı da bir numpy array ile bir zeros fonk olusturduk'\
    'bize 0 değerlerini göndermesi i.in'
    #resim=np.zeros((600,600,3),dtype="uint8")

    #resimden alınan bilgileri değiskenlere atadık
    yukseklik,genislik,kanal=resim.shape

    'resimisleme de ki fonk kullanduk ve onu değişkene atayarak ' \
    'ret ettik'
    resimislema=resimisleme(resim,yukseklik,genislik)

    return resimislema

def resimisleme(resim,yukseklik,genislik):

    birincipixeluzun=45
    ikincipixeluzun=genislik-45
    birincipixelkısa=100
    ikincipixelkısa=genislik-100
    arttirma=60

    for i in range(0,yukseklik,arttirma):
        cizgidengesi(resim,birincipixeluzun,ikincipixeluzun,i)
        cizgidengesi(resim,birincipixelkısa,ikincipixelkısa,int(i+(arttirma/2)))

    dengecizgisi(resim)

    return resim

def cizgidengesi(resim,birincipixel,ikincipixel,artma):

    cizgiresim=cv2.line(resim#işlecek resmimiz
                        ,(birincipixel, artma) #pt1 kordinat sisteminde birinci pixel
                        ,(ikincipixel, artma)#pt2 kodinat sisteminde 2. pixel
                        ,color=(b, g, r)# ilgili resmimiz
                        ,thickness=1)# çizgi kalınlıgı

    return cizgiresim#gelen resmi return ettik

def dengecizgisi(resim):

    #bir cizgi çizemesini istedik
    cv2.line(resim #cizgi olarak işlenilen resim
             ,(100,int(resim.shape[0]/2))# pt1 ile tam merkezde bir çizgi çizdiyoruz
             ,(550,int(resim.shape[0]/2)),#pt2 ile merkezde bir cizgi çizdiyoruz
             (170,0,r),#cizginin resmi
             thickness=1)#cizgi kalınlıgı

    #tam merkezde bir diare çizmesini istedik
    cv2.circle(resim#işlenecek resim
               ,(int(resim.shape[1]/2)
                ,int(resim.shape[0]/2))
               ,radius=25,#dairenini yarı capı
               color=(255,255,255)#dairenin rengi
               ,thickness=1)#dairenin cizgi

    return resim #gelen resmi return ettik

