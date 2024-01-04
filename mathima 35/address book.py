import tkinter as tk
from tkinter import messagebox


class AddressBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book")  # Corrected typo in title

        self.contact_listbox = tk.Listbox(master, width=40, height=10)
        self.contact_listbox.pack(pady=10)

        self.contacts = ["John Doe", "Jane Smith", "Bob Johnson"]
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact)

        self.new_contact_entry = tk.Entry(master, width=30)
        self.new_contact_entry.pack(pady=5)

        add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        add_button.pack(side=tk.LEFT, padx=5)
        remove_button = tk.Button(master, text="Remove Contact", command=self.remove_contact)
        remove_button.pack(side=tk.LEFT, padx=5)

        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_contacts)  # Corrected method name
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.destroy)

    def add_contact(self):
        new_contact = self.new_contact_entry.get()
        if new_contact:
            self.contacts.append(new_contact)
            self.contact_listbox.insert(tk.END, new_contact)
            self.new_contact_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a contact name")

    def remove_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact_to_remove = self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
            messagebox.showinfo("Removed", f"Contact '{contact_to_remove}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to remove")

    def save_contacts(self):
        messagebox.showinfo("Saved", "Contacts save")


def main():
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
