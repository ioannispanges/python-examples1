import tkinter as tk


def open_window():
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_label = tk.Label(new_window, text="Hello for the new window!")
    new_label.pack()


window = tk.Tk()
window.title("Main Window")

open_window_button = tk.Button(window, text="Open new Window", command=open_window)
open_window_button.pack()

window.mainloop()
