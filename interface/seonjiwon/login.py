import tkinter as tk
from tkinter import messagebox
from user import userMenu
from administrator import adminMenu
from user import createAccount


class LoginPage(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("로그인")
        self.root.geometry("400x250")

        self.create_window()

    def create_window(self):
        # 사용자 이름 입력 필드
        self.username_label = tk.Label(self, text="사용자 이름:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # 비밀번호 입력 필드
        self.password_label = tk.Label(self, text="비밀번호:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # 로그인 버튼
        self.login_button = tk.Button(
            self, text="로그인", command=self.check_credentials
        )
        self.login_button.pack()

        # 회원가입 버튼
        self.create_account_button = tk.Button(
            self, text="회원가입", command=self.create_account_page
        )
        self.create_account_button.pack()

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # 여기에 실제로는 데이터베이스나 다른 인증 메커니즘을 통해 인증을 수행할 수 있습니다.
        # 여기서는 간단히 하드코딩된 사용자 이름과 비밀번호를 확인하는 예제를 제공합니다.
        if username == "1" and password == "1":
            messagebox.showinfo("알림", "사용자님 환영합니다!", icon="info")
            self.user_menu_page()
        elif username == "2" and password == "2":
            messagebox.showinfo("알림", "관리자님 환영합니다.", icon="info")
            self.admin_menu_page()
        else:
            messagebox.showerror(
                "로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다."
            )

    def user_menu_page(self):
        # 로그인 페이지 숨기기
        self.pack_forget()
        # 사용자 기능 페이지 표시
        userMenu.showPage(self.root)

    def admin_menu_page(self):
        # 로그인 페이지 숨기기
        self.pack_forget()
        # 관리자 기능 페이지 표시
        adminMenu.showPage(self.root)

    def create_account_page(self):
        # 로그인 페이지 숨기기
        self.pack_forget()
        # 사용자 기능 페이지 표시
        createAccount.showPage(self.root, self)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    app.pack()
    root.mainloop()
