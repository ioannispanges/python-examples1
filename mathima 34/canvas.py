import tkinter as tk

window = tk.Tk()
window.title("Canvas Example")

canvas = tk.Canvas(window, width=500, height=100)
canvas.pack()

canvas.create_rectangle(70, 25, 150, 76, fill="blue")
canvas.create_line(50, 20, 130, 76, fill="green")

window.mainloop()
