import tkinter as tk
from tkinter import messagebox

class User(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("사용자 메뉴")

        label_title = tk.Label(self, text="사용자 메뉴", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        button_option1 = tk.Button(self, text="옵션 1", command=self.option1)
        button_option1.pack(pady=10)

        button_option2 = tk.Button(self, text="옵션 2", command=self.option2)
        button_option2.pack(pady=10)

        button_option3 = tk.Button(self, text="옵션 3", command=self.option3)
        button_option3.pack(pady=10)

    def option1(self):
        messagebox.showinfo("옵션 1", "사용자 메뉴 - 옵션 1 선택")

    def option2(self):
        messagebox.showinfo("옵션 2", "사용자 메뉴 - 옵션 2 선택")

    def option3(self):
        messagebox.showinfo("옵션 3", "사용자 메뉴 - 옵션 3 선택")

class Admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("관리자 메뉴")

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
