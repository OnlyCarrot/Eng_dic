import tkinter as tk
from tkinter import messagebox
from user import userLevelTest


def showPage(root, login_frame):
    # 회원가입 페이지 윈도우 생성
    register_window = tk.Toplevel(root)
    register_window.title("회원가입 페이지")
    register_window.geometry("400x250")

    # 기능 페이지 프레임
    create_account_frame = tk.Frame(register_window)

    # 사용자 이름 입력 필드
    username_label = tk.Label(create_account_frame, text="사용자 이름:")
    username_label.pack()
    username_entry = tk.Entry(create_account_frame)
    username_entry.pack()

    # 비밀번호 입력 필드
    password_label = tk.Label(create_account_frame, text="비밀번호:")
    password_label.pack()
    password_entry = tk.Entry(create_account_frame, show="*")
    password_entry.pack()

    # 회원가입 버튼 클릭 시 실행되는 함수
    def register():
        # 여기에 회원가입 기능을 추가할 수 있습니다.
        # 이 예시에서는 간단히 회원가입 완료 메시지를 표시하고 로그인 화면으로 전환합니다.
        messagebox.showinfo("알림", "회원가입이 완료되었습니다.")
        # 로그인 화면으로 전환
        root.title("로그인")
        login_frame.pack()
        register_window.destroy()

    def level_test():
        userLevelTest.showPage(register_window, create_account_frame)

    # 레벨테스트 버튼
    btn_level_test = tk.Button(
        create_account_frame, text="레벨테스트", command=level_test
    )
    btn_level_test.pack()

    # 회원가입 버튼
    btn_create_account = tk.Button(
        create_account_frame, text="회원가입", command=register
    )
    btn_create_account.pack()

    create_account_frame.pack()
