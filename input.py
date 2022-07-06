import cv2

capture = cv2.VideoCapture(0)
ret, frame = capture.read()

tracker = cv2.TrackerMIL_create()

bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)
font = cv2.FONT_HERSHEY_SIMPLEX

def drawBox(frame, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (255, 0, 0), 3, 1)
    cv2.putText(frame, 'Tracking', (15, 70), font, 0.5, (0, 0, 255), 2)

while (True):
    timer = cv2.getTickCount()
    ret, frame = capture.read()

    ret, bbox = tracker.update(frame)

    if ret:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame, 'Tracking Lost', (15, 70), font, 0.5, (0,0,255),2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()