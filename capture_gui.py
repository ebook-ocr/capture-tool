import customtkinter as ctk
import tkinter.filedialog as fd

def choose_dir():
    path = fd.askdirectory()
    if path:
        folder_entry.delete(0, ctk.END)
        folder_entry.insert(0, path)

def start_capture():
    folder = folder_entry.get()
    prefix = filename_entry.get()
    print(f"保存先: {folder}")
    print(f"ファイル名: {prefix}")
    # TODO: Kindle最大化＋ページ送り＋キャプチャ実装

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x250")
app.title("Kindleキャプチャツール")

ctk.CTkLabel(app, text="保存先フォルダ").pack(pady=5)
folder_entry = ctk.CTkEntry(app, width=300)
folder_entry.pack()
ctk.CTkButton(app, text="フォルダを選ぶ", command=choose_dir).pack(pady=5)

ctk.CTkLabel(app, text="ファイル名（例：page_）").pack(pady=5)
filename_entry = ctk.CTkEntry(app, width=300)
filename_entry.pack()

ctk.CTkButton(app, text="キャプチャ開始", command=start_capture).pack(pady=20)

app.mainloop()
