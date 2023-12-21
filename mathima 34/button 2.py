import tkinter as tk


def on_button_click(event):
    print(f"Button clicked at({event.x}, {event.y})")


window = tk.Tk()
window.title("Event Handling Example")
window.geometry("400x200")

button = tk.Button(window, text="Click me")
button.bind("<Button-1>", on_button_click)
button.pack(pady=100, padx=100)

window.mainloop()
