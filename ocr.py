from PIL import Image
import pytesseract

def ocr_image_to_text(path: str) -> str:
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
    image = Image.open(path)
    text = pytesseract.image_to_string(image, lang="jpn")
    return text.strip()