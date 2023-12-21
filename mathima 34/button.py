import tkinter as tk


def on_button_click():
    print("Button clicked")


window = tk.Tk()
window.title("Event Handling Example")

button = tk.Button(window, text="Click me", command=on_button_click)
button.pack()

window.mainloop()
