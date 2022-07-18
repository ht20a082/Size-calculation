import cv2
from libzbar import zbar
import numpy as np


capture = cv2.VideoCapture(0)


# zbar
scanner = zbar.ImageScanner()
scanner.parse_config('enable')


while (True):
    timer = cv2.getTickCount()
    frame = capture.read()

    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    small_image = cv2.resize(image, dsize=(480,360))

    gray_image = cv2.cvtColor(small_image, cv2.COLOR_BGR2GRAY)
    rows, cols = gray_image.shape[:2]
    image = zbar.Image(cols, rows, 'Y800', gray_image.tostring())

    scanner.scan(image)


    for symbol in image:
        qr_type = symbol.type
        qr_msg = symbol.data
        qr_positions = symbol.location
        print('QR code : %s, %s, %s'%(qr_type, qr_msg, str(qr_positions)))
        
        pts = np.array(qr_positions)
        cv2.polylines(small_image, [pts], True, (0,255,0), thickness=3)

    del image

    cv2.imshow('frame', small_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()