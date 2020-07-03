
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\59596\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image


img = Image.open('2.jpeg')
text = tess.image_to_string(img)

print(text)