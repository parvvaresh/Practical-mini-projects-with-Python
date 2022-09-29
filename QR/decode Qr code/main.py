import cv2
import barcode
from pyzbar.pyzbar import decode


def read_qr(path):
  text = ""
  img = cv2.imread(path)
  for barcode in decode(img):
    text = barcode.data.decode("utf-8")
  print("your Qr code ---- >" + "\n" + "---------------->" + text)


path = "C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\\simple project\\Qr code\\De code Qr\\Qr.png"

read_qr(path)


