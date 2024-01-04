import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display_entry = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.display_entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val, col_val = 1, 0
        for button in buttons:
            (tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5))
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_text = self.display_entry.get()

        if value == '=':
            try:
                result = str(eval(current_text))
                self.display_entry.delete(0, tk.END)
                self.display_entry.insert(tk.END, result)
            except Exception:
                self.display_entry.delete(0, tk.END)
                self.display_entry.insert(tk.END, "Error")
        else:
            self.display_entry.insert(tk.END, value)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
