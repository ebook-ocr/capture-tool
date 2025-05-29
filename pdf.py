import os

def build_pdf_path(folder: str, filename: str) -> str:
    return os.path.join(folder, f"{filename}.pdf")