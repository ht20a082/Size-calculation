import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    ret,frame = cap.read()

    if ret:
        value = decode(frame, symbols = [ZBarSymbol.QRCODE])
        if value:
            for qrcode in value:
                x, y, w, h = qrcode.rect

                dec_inf = qrcode.data.decode('utf-8')
                print('dec:', dec_inf)
                frame = cv2.putText(frame, dec_inf, (x, y-6), font, .3, (255,0,0), 1, cv2.LINE_AA)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)

        cv2.imshow('pyzbar', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
