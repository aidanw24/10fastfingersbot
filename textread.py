import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\\Program Files\Tesseract-OCR\tesseract.exe'


def reader():
    img = Image.open('element.png')
    text = pytesseract.image_to_string(img, lang='eng')
    words = text.split()
    return words
