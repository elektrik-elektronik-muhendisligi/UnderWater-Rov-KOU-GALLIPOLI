import  cv2
import numpy as np

kamera=cv2.VideoCapture(0)

def camera():
    while True:
        ret,kare=kamera.read()

        #cv2.imshow("Kmare",kare)

        return kare,kare

        if cv2.waitKey(25)&0xFF==ord("q"):
            break
            kamera.release()
            cv2.destroyAllWindows()




if __name__ == '__main__':
    camera()