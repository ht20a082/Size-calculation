import cv2

image = cv2.imread("qrcode_test.png")

qrDetector = cv2.QRCodeDetector()

data,bbox,rectifiedImage = qrDetector.detectAndDecode(image)

print(data)

if(data == "QI code landmarks"):
    print("true")