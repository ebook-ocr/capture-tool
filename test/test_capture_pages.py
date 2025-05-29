from capture_pages import capture_pages
import os

def test_capture_pages(tmp_path, monkeypatch):
    folder = tmp_path
    prefix = "page_"
    start = 1
    end = 3
    saved_files = []

    # pyautoguiのモック
    class DummyScreenshot:
        def save(self, path): saved_files.append(path)

    monkeypatch.setattr("pyautogui.screenshot", lambda: DummyScreenshot())
    monkeypatch.setattr("pyautogui.press", lambda key: None)

    paths = capture_pages(folder, prefix, start, end)

    assert len(paths) == 3
    for i, path in enumerate(paths, start=1):
        expected_name = f"{prefix}{i:03}.png"
        assert path.endswith(expected_name)
        assert os.path.basename(path) in [os.path.basename(p) for p in saved_files]
