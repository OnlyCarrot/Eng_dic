import tkinter as tk
from tkinter import messagebox
import pandas as pd

class WordEditor:
    def __init__(self, master, file_path):
        self.master = master
        self.file_path = file_path
        self.current_page = 0
        self.words_per_page = 10
        self.word_checkboxes = []

        self.load_data()

        self.create_widgets()

    def load_data(self):
        try:
            self.df = pd.read_excel(self.file_path, sheet_name='wordsheet')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
            self.master.destroy()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.master, width=50, height=self.words_per_page)
        self.listbox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.prev_button = tk.Button(self.master, text="Previous", command=self.prev_page)
        self.prev_button.grid(row=1, column=0, padx=5, pady=5)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_page)
        self.next_button.grid(row=1, column=1, padx=5, pady=5)

        self.edit_button = tk.Button(self.master, text="Edit", command=self.edit_word)
        self.edit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.update_listbox()

    def update_listbox(self):
        start_idx = self.current_page * self.words_per_page
        end_idx = min((self.current_page + 1) * self.words_per_page, len(self.df))

        self.listbox.delete(0, tk.END)
        self.word_checkboxes.clear()  # Clear the checkboxes list
        for idx in range(start_idx, end_idx):
            word = self.df.iloc[idx]['Eng']
            self.listbox.insert(tk.END, word)
            checkbox_var = tk.BooleanVar()
            self.word_checkboxes.append(checkbox_var)  # Append the checkbox variable
            tk.Checkbutton(self.master, variable=checkbox_var).grid(row=idx % self.words_per_page, column=2)

    def next_page(self):
        max_pages = len(self.df) // self.words_per_page
        if self.current_page < max_pages:
            self.current_page += 1
            self.update_listbox()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_listbox()

    def edit_word(self):
        selected_indices = [i for i, checkbox in enumerate(self.word_checkboxes) if checkbox.get()]
        if not selected_indices:
            messagebox.showwarning("Warning", "Please select a word to edit.")
            return

        selected_index = selected_indices[0]
        word = self.listbox.get(selected_index)

        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Word")

        tk.Label(edit_window, text="English Word:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Korean Meaning:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Part of Speech:").grid(row=2, column=0, padx=5, pady=5)

        self.eng_var = tk.StringVar()
        self.kor_var = tk.StringVar()
        self.pos_var = tk.StringVar()

        self.eng_var.set(self.df.iloc[selected_index]['Eng'])
        self.kor_var.set(self.df.iloc[selected_index]['Kor'])
        self.pos_var.set(self.df.iloc[selected_index]['WC'])

        tk.Entry(edit_window, textvariable=self.eng_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(edit_window, textvariable=self.kor_var).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(edit_window, textvariable=self.pos_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(edit_window, text="Update", command=lambda: self.update_word(selected_index, edit_window)).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def update_word(self, index, window):
        new_eng = self.eng_var.get()
        new_kor = self.kor_var.get()
        new_pos = self.pos_var.get()

        if not new_eng.strip() and not new_kor.strip() and not new_pos.strip():
            messagebox.showwarning("Warning", "Please update at least one field.")
            return

        self.df.at[index, 'Eng'] = new_eng
        self.df.at[index, 'Kor'] = new_kor
        self.df.at[index, 'WC'] = new_pos

        self.df.to_excel(self.file_path, index=False)

        messagebox.showinfo("Success", "Word updated successfully.")

        window.destroy()
        self.update_listbox()

def main():
    file_path = r"C:\Eng_dic\interface\OnlyCarrot\WordList.xlsx"
    root = tk.Tk()
    root.title("Word Editor")
    editor = WordEditor(root, file_path)
    root.mainloop()

if __name__ == "__main__":
    main()
