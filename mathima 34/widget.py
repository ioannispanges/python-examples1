import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Styled Button Example")

style = ttk.Style()

style.configure("TButton", foreground="green", font=("Arial", 12, "bold"))

styled_button = ttk.Button(window, text="Styled Button", style="TButton")
styled_button.pack()

window.mainloop()
