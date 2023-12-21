import tkinter as tk


def open_new_window():
    new_window = tk.Toplevel(window)
    new_window.title("New window")


window = tk.Tk()
window.title("Main Window")

open_window_button = tk.Button(window, text="Open New window", command=open_new_window)
open_window_button.pack()

window.mainloop()
