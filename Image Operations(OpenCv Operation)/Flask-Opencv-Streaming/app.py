#!/usr/bin/env python
from flask import Flask, render_template, Response #burada flask kütüphanesinden parçalarımızı cıkardık
import cv2 # opencv kütüpahensini ekledik
import numpy as np

image =np
app = Flask(__name__) #flask ı bu saftada entegre ettik
video = cv2.VideoCapture(0) # opencv kütüpahensi ile
''' bu kameradan bilgi almasını istedik'''

'burada sayfaya ilk girildiğinde bize html bilgisini göstermesini istedik'
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
    'burada template ile index.html bilgisini göstermesini istedik'


def gen():
    """Burada sonsuz bir döngü oluşturarak Streaming bir şekilde resmimizi kaydetip okuma işlemleri ypaıyoruz"""
    while True:
        rval, frame = video.read()
        image=frame
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

        '''yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')'''


@app.route('/video_feed')
def video_feed():
    """burada amaç ise index.html sayfasına ihtiyaç duymadan anlık olarak verilerimizi kaydetip çekebiliyoruz
    Response ise burada cevap almamıızı sağlıyor
    -Sayfaya istek atıyoruz atılan isteğe göre bir Response dönüyor ancak verimiz
    sürekli olması gerektiği için Response ile sarmalayıp mimetype ile gerş dönüşü belli ediyoruz...
    """
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, threaded=True,port=9875)
