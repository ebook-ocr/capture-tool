import os

def test_print():
    current_dir = os.getcwd()
    print(f"current_dir:\n {current_dir}")

    script_path = os.path.abspath(__file__)
    print(f"script_path:\n {script_path}")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"script_dir:\n {script_dir}")

    print(f"__file__:\n {__file__}")