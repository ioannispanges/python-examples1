import tkinter as tk


def cut_function():
    print("Cut function called")


def copy_function():
    print("Copy function called")


def paste_function():
    print("Paste function called")


window = tk.Tk()
window.title("Edit Menu Example")

menu_bar = tk.Menu(window)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_function)
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=copy_function)
edit_menu.add_command(label="Paste", command=paste_function)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
window.config(menu=menu_bar)
window.mainloop()
