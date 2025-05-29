import pyautogui
import os

def capture_screenshot(folder: str, filename: str) -> str:
    path = os.path.join(folder, f"{filename}.png")
    image = pyautogui.screenshot()
    image.save(path)
    return path
