import cv2

capture = cv2.VideoCapture(0)

tracker = cv2.TrackerMIL_create()
success, img = capture.read()

bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)
font = cv2.FONT_HERSHEY_SIMPLEX

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255, 0, 0), 3, 1)
    cv2.putText(img, 'Tracking', (15, 70), font, 0.5, (0, 0, 255), 2)

while (True):
    timer = cv2.getTickCount()
    sccess, img = capture.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, 'Tracking Lost', (15, 70), font, 0.5, (0,0,255),2)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()