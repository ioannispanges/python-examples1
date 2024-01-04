import tkinter as tk
from tkinter import filedialog


class FileExplorerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Explorer")
        self.file_path_entry = tk.Entry(master, width=50)
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        open_button = tk.Button(master, text="Open File", command=self.open_file_dialog)
        open_button.grid(row=1, column=0, padx=10, pady=10)

        open_dir_button = tk.Button(master, text="Open Directory", command=self.open_directory_dialog)
        open_dir_button.grid(row=1, column=0, padx=10, pady=10)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(tk.END, file_path)

    def open_directory_dialog(self):
        dir_path = filedialog.askdirectory(title="Select a Directory")
        if dir_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(tk.END, dir_path)


def main():
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
