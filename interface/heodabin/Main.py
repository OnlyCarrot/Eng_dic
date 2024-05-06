import tkinter as tk
import os

def open_login_page():
    os.system('python Login.py')

def open_register_page():
    os.system('python Register.py')

# 메인 윈도우 생성
root = tk.Tk()
root.title("메인 화면")

# 로그인 버튼
login_button = tk.Button(root, text="로그인", command=open_login_page)
login_button.pack(pady=20)

# 회원가입 버튼
register_button = tk.Button(root, text="회원가입", command=open_register_page)
register_button.pack(pady=20)

# 프로그램 실행
root.mainloop()
