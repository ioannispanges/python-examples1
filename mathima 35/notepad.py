import tkinter as tk
from tkinter import filedialog


class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")

        self.note_text = tk.Text(master, wrap=tk.WORD, width=40, height=10)
        self.note_text.pack(padx=10, pady=10)

        save_button = tk.Button(master, text="Save", command=self.save_note)
        save_button.pack(side=tk.LEFT, padx=5)

        load_button = tk.Button(master, text="Load", command=self.load_note)
        load_button.pack(side=tk.LEFT, padx=5)

    def save_note(self):
        note_content = self.note_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write(note_content)
            tk.messagebox.showinfo("Saved", "Note saved successfully")

    def load_note(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            with open(file_path, "r") as file:
                note_content = file.read()
                self.note_text.delete("1.0", tk.END)
                self.note_text.insert(tk.END, note_content)

    def clear_note(self):
        self.note_text.delete("1.0", tk.END)


def main():
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
