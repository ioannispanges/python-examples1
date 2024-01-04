import tkinter as tk

window = tk.Tk()
window.title("Canvas Drawing Example")

canvas = tk.Canvas(window, width=200, height=150)
canvas.pack()

canvas.create_line(0, 0, 100, 100, fill="red", width=2)

canvas.create_oval(50, 50, 150, 100, fill="yellow")
window.mainloop()
