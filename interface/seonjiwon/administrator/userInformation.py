import tkinter as tk
from tkinter import messagebox


def showPage(previous_window, previous_frame):
    # 레벨테스트 페이지 윈도우 생성
    user_information_windoe = tk.Toplevel(previous_window)
    user_information_windoe.title("단어장")
    user_information_windoe.geometry("600x450")

    # 레벨테스트 페이지 프레임
    user_information_frame = tk.Frame(user_information_windoe)

    # 사용자 단어 입력 필드
    test_lable = tk.Label(user_information_frame, text="회원 정보")
    test_lable.pack()

    # 회원가입 버튼 클릭 시 실행되는 함수
    def finish():
        messagebox.showinfo("알림", "회원 조회가 종료되었습니다.")
        # 회원가입
        previous_window.title("관리자 페이지")
        previous_frame.pack()
        user_information_windoe.destroy()

    # 완료 버튼
    btn_finish = tk.Button(user_information_frame, text="완료", command=finish)
    btn_finish.pack()

    user_information_frame.pack()
