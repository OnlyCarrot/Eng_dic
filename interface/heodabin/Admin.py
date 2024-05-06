import tkinter as tk
from tkinter import messagebox

class Admin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label_title = tk.Label(self, text="관리자 메뉴", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        button_option1 = tk.Button(self, text="옵션 A", command=self.optionA)
        button_option1.pack(pady=10)

        button_option2 = tk.Button(self, text="옵션 B", command=self.optionB)
        button_option2.pack(pady=10)

        button_option3 = tk.Button(self, text="옵션 C", command=self.optionC)
        button_option3.pack(pady=10)

    def optionA(self):
        messagebox.showinfo("옵션 A", "관리자 메뉴 - 옵션 A 선택")

    def optionB(self):
        messagebox.showinfo("옵션 B", "관리자 메뉴 - 옵션 B 선택")

    def optionC(self):
        messagebox.showinfo("옵션 C", "관리자 메뉴 - 옵션 C 선택")
