import tkinter as tk
from tkinter import messagebox

# 이 함수는 로그인 화면을 보여주는 함수
def ShowLogin():
    # tkinter 창 생성
    root = tk.Tk()
    root.title("로그인")

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

    # 로그인 버튼
    login_button = tk.Button(root, text="로그인", command=lambda: Login(entry_id.get(), entry_pw.get(), root))
    login_button.grid(row=2, columnspan=2)

    # Home 버튼
    home_button = tk.Button(root, text="Home", command=ShowHome)
    home_button.grid(row=0, column=3)

    # GUI 실행
    root.mainloop()

# 이 함수는 사용자가 입력한 정보를 확인하고 로그인을 처리
def Login(input_id, input_pw, root):
    #if input_id in DB and input_pw in DB
    
    # 여기서는 데이터베이스가 없으니까 간단히 ID가 "user", 비밀번호가 "password"인 경우에만 로그인 성공으로 처리
    if input_id == "user" and input_pw == "pw":
        messagebox.showinfo("로그인 성공", "로그인 성공했습니다.")
        # 이 부분에 따라 user나 admin을 반환, 일단 메시지 출력
    else:
        messagebox.showerror("로그인 실패", "ID 혹은 비밀번호가 잘못되었습니다.")

    # 로그인 후에는 로그인 창을 닫고 메인 창을 열도록 설정
    #root.destroy()

# interface.py에 있는 ShowHome 함수를 여기에 작성했다고 가정하고, 간단하게 print
def ShowHome():
    messagebox.showinfo("ShowUpHome", "Home 창을 보여줍니다.")

# 로그인 화면 보여주기
ShowLogin()

