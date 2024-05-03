import tkinter as tk
from tkinter import messagebox


def showPage(previous_window, previous_frame):
    # 레벨테스트 페이지 윈도우 생성
    level_test_window = tk.Toplevel(previous_window)
    level_test_window.title("레벨테스트")
    level_test_window.geometry("600x450")

    # 레벨테스트 페이지 프레임
    level_test_frame = tk.Frame(level_test_window)

    # 사용자 단어 입력 필드
    test_lable = tk.Label(level_test_frame, text="단어 뜻")
    test_lable.pack()
    test_entry = tk.Entry(level_test_frame)
    test_entry.pack()

    # 회원가입 버튼 클릭 시 실행되는 함수
    def finish():
        messagebox.showinfo("알림", "레벨테스트가 완료되었습니다.")
        # 회원가입
        previous_window.title("회원가입 페이지")
        previous_frame.pack()
        level_test_window.destroy()

    # 완료 버튼
    btn_finish = tk.Button(level_test_frame, text="완료", command=finish)
    btn_finish.pack()

    level_test_frame.pack()
