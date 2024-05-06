from tkinter import *
from center_window import center_window

class ViewLevelPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("사용자별 레벨 조회")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="사용자별 레벨 조회 페이지")
        label.pack(pady=10)

        # Add your view level by user functionality here

        # Back to Admin Page Button
        back_button = Button(self.window, text="관리자 페이지로 돌아가기", command=self.back_to_admin)
        back_button.pack(pady=5)

    def back_to_admin(self):
        # Destroy the current window and show the admin page window
        self.window.destroy()
        self.parent.deiconify()

class ViewDistributionPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("사용자 전체 레벨 분포")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="사용자 전체 레벨 분포 페이지")
        label.pack(pady=10)

        # Add your view level distribution by user functionality here  

        # Back to Admin Page Button
        back_button = Button(self.window, text="관리자 페이지로 돌아가기", command=self.back_to_admin)
        back_button.pack(pady=5)

    def back_to_admin(self):
        # Destroy the current window and show the admin page window
        self.window.destroy()
        self.parent.deiconify()
