from PIL import Image
import cv2
import os
import pytesseract
from pytesseract import image_to_string
import sys

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

name='./licensePlatePath/'+sys.argv[1]
im=cv2.imread(name)
print("Final plate:")
print (image_to_string(im))

#print (image_to_string(Image.open('car.jpg'), lang='eng'))