import tkinter as tk


def open_file():
    print("Open file function called")


def toggle_option():
    option_value = option_var.get()
    print(f"Option toggled:{option_value}")


window = tk.Tk()
window.title("Menu Example")

option_var = tk.BooleanVar()
option_var.set(False)

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_separator()
file_menu.add_checkbutton(label="Toggle Option", variable=option_var, command=toggle_option)

menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()
