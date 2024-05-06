from tkinter import *
from center_window import center_window

class AddWordPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("단어 추가")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="단어 추가 페이지")
        label.pack(pady=10)

        # Back to Admin Page Button
        back_button = Button(self.window, text="관리자 페이지로 돌아가기", command=self.back_to_admin)
        back_button.pack(pady=5)

    def back_to_admin(self):
        # Destroy the current window and show the admin page window
        self.window.destroy()
        self.parent.deiconify()

class DeleteWordPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("단어 삭제")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="단어 삭제 페이지")
        label.pack(pady=10)

        # Add your delete word functionality here

        # Back to Admin Page Button
        back_button = Button(self.window, text="관리자 페이지로 돌아가기", command=self.back_to_admin)
        back_button.pack(pady=5)

    def back_to_admin(self):
        # Destroy the current window and show the admin page window
        self.window.destroy()
        self.parent.deiconify()

class EditWordPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("단어 수정")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="단어 수정 페이지")
        label.pack(pady=10)

        # Add your edit word functionality here 

        # Back to Admin Page Button
        back_button = Button(self.window, text="관리자 페이지로 돌아가기", command=self.back_to_admin)
        back_button.pack(pady=5)

    def back_to_admin(self):
        # Destroy the current window and show the admin page window
        self.window.destroy()
        self.parent.deiconify()
