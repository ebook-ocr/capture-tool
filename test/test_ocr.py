from ocr import ocr_image_to_text
from PIL import Image, ImageDraw, ImageFont
import os

def test_orc_image_to_text(tmp_path):
    # テスト画像を作成
    img_path = tmp_path / "hello.png"
    image = Image.new("RGB", (200, 100), color="white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 30), "こんにちは", fill="black")
    image.save(img_path)

    # OCR実行
    text = ocr_image_to_text(str(img_path))
    assert "こんにちは" in text
