import tkinter as tk
from tkinter import filedialog


def ask_file_path():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return path
