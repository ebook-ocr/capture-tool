import os
from capture import capture_screenshot
from pathlib import Path

def test_capture_screenshot(tmp_path):
    # テスト用の保存先とファイル名
    folder = tmp_path
    filename = "test_page"

    # 関数を呼び出し
    path = capture_screenshot(folder, filename)

    # ファイルが存在することを確認
    assert os.path.exists(path)
    assert path.endswith(".png")
