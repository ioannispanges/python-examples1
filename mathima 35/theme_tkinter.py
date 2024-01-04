import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Themed Button Example")

style = ttk.Style()

style.theme_use("clam")

style.configure("TButton", foreground="green", background="lightgray", font=("Arial", 12, "bold"))

styled_button = ttk.Button(window, text="Styled Button", style="TButton")
styled_button.pack()

window.mainloop()
