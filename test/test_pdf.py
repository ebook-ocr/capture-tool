import os
from pdf import build_pdf_path

def test_build_pdf_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = build_pdf_path(f"{script_dir}/test_storage", "mybook")
    assert path == f"{script_dir}/test_storage/mybook.pdf"
