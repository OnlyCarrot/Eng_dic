import tkinter as tk
from tkinter import messagebox


def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    # 여기에 실제로는 데이터베이스나 다른 인증 메커니즘을 통해 인증을 수행할 수 있습니다.
    # 여기서는 간단히 하드코딩된 사용자 이름과 비밀번호를 확인하는 예제를 제공합니다.
    if username == "user" and password == "password":
        messagebox.showinfo("로그인 성공", "환영합니다!")
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")


# Tkinter 윈도우 생성
root = tk.Tk()
root.title("로그인")

# 사용자 이름 입력 필드
username_label = tk.Label(root, text="사용자 이름:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# 비밀번호 입력 필드
password_label = tk.Label(root, text="비밀번호:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# 로그인 버튼
login_button = tk.Button(root, text="로그인", command=check_credentials)
login_button.pack()

# 프로그램 실행
root.mainloop()
