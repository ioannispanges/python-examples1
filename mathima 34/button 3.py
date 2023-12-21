import tkinter as tk

def on_event_handler(_):
    label.config(text="Mouse moved")

root = tk.Tk()
root.title("Event Handling Example")
root.geometry("400x200")


button = tk.Button(root, text="Click me!")
button.bind("<Button-1>", on_event_handler)

label = tk.Label(root, text="Move the mouse over me")
button.bind("<Motion>", on_event_handler)

button.pack()
label.pack()

root.mainloop()


