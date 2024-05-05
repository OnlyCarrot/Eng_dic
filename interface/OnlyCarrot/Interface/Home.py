import tkinter as tk
from tkinter import messagebox
#import login
#import register
#import test
#import voca

# 화면 크기 조절 변수
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

def open_login_window():
    # ToDo: login.py의 로그인 화면을 띄우는 함수 호출
    pass

def open_register_window():
    # ToDo: register.py의 회원가입 화면을 띄우는 함수 호출
    pass

def open_test_window():
    # ToDo: test.py의 영어단어 시험 화면을 띄우는 함수 호출
    pass

def open_voca_window():
    # ToDo: voca.py의 영어단어장 관리 화면을 띄우는 함수 호출
    pass

# 메인 창 생성
root = tk.Tk()
root.title("인터페이스")

# 화면 크기 조절
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# 버튼 레이아웃 조정을 위한 프레임
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill=tk.BOTH)

# 로그인 버튼
login_button = tk.Button(button_frame, text="로그인", command=open_login_window)
login_button.grid(row=0, column=0, padx=10, pady=10)

# 회원가입 버튼
register_button = tk.Button(button_frame, text="회원가입", command=open_register_window)
register_button.grid(row=0, column=1, padx=10, pady=10)

# 영어단어 시험 버튼
test_button = tk.Button(button_frame, text="영어단어 시험", command=open_test_window)
test_button.grid(row=1, column=0, padx=10, pady=10)

# 영어단어장 관리 버튼
voca_button = tk.Button(button_frame, text="영어단어장 관리", command=open_voca_window)
voca_button.grid(row=1, column=1, padx=10, pady=10)

# GUI 실행
root.mainloop()
