# support gif,png ppm/pgm, pem, and xpm formats
import tkinter as tk
from tkinter import filedialog


def open_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        load_and_display_image(image_path)


def load_and_display_image(image_path):
    image = tk.PhotoImage(file=image_path)
    canvas.create_image(20, 20, anchor=tk.NW, image=image)
    canvas.image = image


window = tk.Tk()
window.title("Image on Canvas Example")

canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

open_image_button = tk.Button(window, text="Open Image", command=open_image)
open_image_button.pack()

window.mainloop()
