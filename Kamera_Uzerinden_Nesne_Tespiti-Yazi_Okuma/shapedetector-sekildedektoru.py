# gerekli paketleri içe aktarın
import cv2

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        # şekil adını başlat ve konturu yaklaştır
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        
        #şekil düz bir çizgi ise
        if len(approx) == 2:
            shape = "Line"

        # şekil bir üçgense, 3 köşesi olacaktır
        if len(approx) == 3:
            shape = "triangle"

        # şeklin 4 köşesi varsa, kare veya
        # dikdörtgen şeklindedir
        elif len(approx) == 4:
            # konturun sınırlayıcı kutusunu hesaplayın ve en boy oranını hesaplamak için
            # sınırlayıcı kutuyu kullanın
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # bir kare, yaklaşık olarak bire eşit bir en boy oranına sahip olacaktır, aksi takdirde şekil bir dikdörtgendir
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

        # şekil bir beşgen ise, 5 köşesi olacaktır
        elif len(approx) == 5:
            shape = "pentagon"

        # Aksi takdirde, şeklin bir daire olduğunu varsayarız
        else:
            shape = "circle"

        # şeklin adını döndür
        return shape
