import qrcode
from PIL import Image

img = qrcode.make('QI code landmarks')

print(type(img))
print(img.size)

img.save('qrcode_test.png')