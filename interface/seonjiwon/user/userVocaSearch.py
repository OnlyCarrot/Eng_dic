import tkinter as tk
from tkinter import messagebox


def showPage(previous_window, previous_frame):
    # 레벨테스트 페이지 윈도우 생성
    voca_window = tk.Toplevel(previous_window)
    voca_window.title("단어장")
    voca_window.geometry("600x450")

    # 레벨테스트 페이지 프레임
    voca_frame = tk.Frame(voca_window)

    # 사용자 단어 입력 필드
    test_lable = tk.Label(voca_frame, text="단어 보여주기")
    test_lable.pack()

    # 회원가입 버튼 클릭 시 실행되는 함수
    def finish():
        messagebox.showinfo("알림", "단어장이 종료되었습니다.")
        # 회원가입
        previous_window.title("사용자 페이지")
        previous_frame.pack()
        voca_window.destroy()

    # 완료 버튼
    btn_finish = tk.Button(voca_frame, text="완료", command=finish)
    btn_finish.pack()

    voca_frame.pack()
