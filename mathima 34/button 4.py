import tkinter as tk


def on_button_click(event):
    print("Button Clicked")


def unbind_button_click():
    button.unbind("<Button-1>")
    print("Left mouse button click event unbound")


window = tk.Tk()
window.title("Unbind Example")
button = tk.Button(window, text="Click Me")
button.bind("<Button-1>", on_button_click)
button.pack(pady=20)

unbind_button = tk.Button(window, text="Unbind click event", command=unbind_button_click)
unbind_button.pack(pady=10)

window.mainloop()
