import tkinter as tk
from tkinter import messagebox
from DailyTest import DailyTest # type: ignore
from VocaShow import VocaShow # type: ignore

class User(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label_title = tk.Label(self, text="사용자 메뉴", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        button_option1 = tk.Button(self, text="단어장", command=self.option1)
        button_option1.pack(pady=10)

        button_option2 = tk.Button(self, text="일일테스트", command=self.option2)
        button_option2.pack(pady=10)

        button_option3 = tk.Button(self, text="옵션 3", command=self.option3)
        button_option3.pack(pady=10)

    def option1(self):
        messagebox.showinfo("옵션 1", "사용자 메뉴 - 옵션 1 선택")
        voca_show_window = tk.Toplevel(self.master)
        voca_show = DailyTest(voca_show_window)

    def option2(self):
        messagebox.showinfo("옵션 2", "사용자 메뉴 - 옵션 2 선택")
        daily_test_window = tk.Toplevel(self.master)
        daily_test = DailyTest(daily_test_window)

    def option3(self):
        messagebox.showinfo("옵션 3", "사용자 메뉴 - 옵션 3 선택")
