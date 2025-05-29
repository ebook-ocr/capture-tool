import pyautogui
from capture import capture_screenshot

def capture_pages(folder: str, prefix: str, start: int, end: int) -> list[str]:
    paths = []

    for i in range(start, end + 1):
        filename = f"{prefix}{i:03}"
        path = capture_screenshot(folder, filename)
        paths.append(path)
        pyautogui.press("right")

    return paths
