import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilenames()
    if file_path:
        print(f"Opened file:{file_path}")


def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        print(f"Save file:{file_path}")


window = tk.Tk()
window.title("Simple file Menu Example")

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()
