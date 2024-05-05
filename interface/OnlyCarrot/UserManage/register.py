import tkinter as tk
from tkinter import messagebox

# 다음 화면으로 넘어가는 함수
def NextStep(entry_id, entry_pw, entry_name, root):
    # 이 부분에서는 간단히 입력된 정보를 출력하는 것으로 가정
    messagebox.showinfo("회원가입 완료", f"다음 정보로 회원가입이 완료되었습니다:\nID: {entry_id.get()}\n비밀번호: {entry_pw.get()}\n이름: {entry_name.get()}")
    
    # 다음 화면으로 이동
    root.destroy()
    ShowLevelTest()

# 회원가입 화면을 보여주는 함수
def ShowRegister():
    # tkinter 창 생성
    root = tk.Tk()
    root.title("회원가입")

    # ID 입력 라벨과 입력창 생성
    label_id = tk.Label(root, text="ID: ")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1)

    # 비밀번호 입력 라벨과 입력창 생성
    label_pw = tk.Label(root, text="비밀번호: ")
    label_pw.grid(row=1, column=0)
    entry_pw = tk.Entry(root, show="*")
    entry_pw.grid(row=1, column=1)

    # 이름 입력 라벨과 입력창 생성
    label_name = tk.Label(root, text="이름: ")
    label_name.grid(row=2, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=2, column=1)
    """
    entry_id, entry_pw, entry_name DB에 저장하는 코드
    """
    # 다음 버튼
    next_button = tk.Button(root, text="다음", command=lambda: NextStep(entry_id, entry_pw, entry_name, root))
    next_button.grid(row=3, columnspan=2)

    # Home 버튼
    home_button = tk.Button(root, text="Home", command=ShowHome)
    home_button.grid(row=0, column=2)

    # GUI 실행
    root.mainloop()

# 사용자 레벨 테스트 화면을 보여주는 함수
def ShowLevelTest():
    # tkinter 창 생성
    test_window = tk.Tk()
    test_window.title("레벨 테스트")

    # 테스트 문구
    test_label = tk.Label(test_window, text="사용자의 레벨을 테스트 합니다. 문제는 40문제입니다.")
    test_label.pack()

    # 시작 버튼
    start_button = tk.Button(test_window, text="시작", command=lambda: messagebox.showinfo("시험시작", "시험을 시작합니다.")) #Test에서 LevelTest 호출
    start_button.pack()

    # Home 버튼
    home_button = tk.Button(test_window, text="Home", command=ShowHome)
    home_button.pack()

    # GUI 실행
    test_window.mainloop()

# interface.py에 있는 ShowHome 함수를 여기에 작성했다고 가정하고, 간단하게 print
def ShowHome():
    messagebox.showinfo("ShowUpHome", "Home 창을 보여줍니다.")

# 회원가입 화면 보여주기
ShowRegister()
