from tkinter import *
from tkinter import messagebox
from User.test import LevelTestScreen  # Importing the LevelTestScreen class from test.py
from center_window import center_window  # center_window 모듈 가져오기

class SignupPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("회원가입")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="회원가입 페이지")
        label.pack(pady=10)

        # Username Entry
        self.username_label = Label(self.window, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self.window)
        self.username_entry.pack()

        # Password Entry
        self.password_label = Label(self.window, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.window, show="*")
        self.password_entry.pack()

        # Signup Button
        self.signup_button = Button(self.window, text="회원가입", command=self.signup)
        self.signup_button.pack(pady=10)

    def signup(self):
        # Get username and password from entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add your signup functionality here
        register_good = "회원가입 성공"
        welcome_message = f"환영합니다, {username}님. 레벨 테스트를 시작합니다.😊😊"
        messagebox.showinfo(register_good, welcome_message)

        # After signup, open the level test screen
        self.open_level_test_screen()

    def open_level_test_screen(self):
        # Open the level test screen
        self.window.withdraw()  # Hide the signup window
        LevelTestScreen(self.parent)
