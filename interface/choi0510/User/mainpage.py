from tkinter import *
from tkinter import messagebox
from User.Voca import Show  # Importing the Show class from Voca.py
from User.test import DailyTestScreen  # Importing the DailyTestScreen class from test.py
from center_window import center_window

class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("수준별 토익 영단어 프로그램")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="function")
        label.pack(pady=10)

        search_button = Button(self.window, text="일일테스트 보기", command=self.open_daily_test_screen)
        search_button.pack(pady=5)

        delete_button = Button(self.window, text="단어장 조회하기", command=self.open_show_screen)
        delete_button.pack(pady=5)

        close_button = Button(self.window, text="로그인 화면으로", command=self.close_main_page)
        close_button.pack(pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.parent.withdraw()

    def close_main_page(self):
        self.window.destroy()
        self.parent.deiconify()

    def on_close(self):
        self.parent.deiconify()
        self.window.destroy()

    def open_daily_test_screen(self):
        self.window.withdraw()  # Hide the main window
        DailyTestScreen(self.window)  # Open the DailyTestScreen

    def open_show_screen(self):
        self.window.withdraw()  # Hide the main window
        Show(self.window)  # Open the Show screen
