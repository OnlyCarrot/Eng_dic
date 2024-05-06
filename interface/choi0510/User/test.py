from tkinter import *
from center_window import center_window  # center_window 모듈 가져오기

class LevelTestScreen:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("레벨 테스트")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="레벨 테스트 페이지")
        label.pack(pady=10)

        self.back_button = Button(self.window, text="돌아가기", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.parent.deiconify()


class DailyTestScreen:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("일일 테스트")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="일일 테스트 페이지")
        label.pack(pady=10)

        self.back_button = Button(self.window, text="돌아가기", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.window.destroy()
        self.parent.deiconify()
