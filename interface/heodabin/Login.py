import tkinter as tk
from tkinter import messagebox
import openpyxl
from User import User # type: ignore
from Admin import Admin # type: ignore

def authenticate_user(id, password):
    try:
        wb = openpyxl.load_workbook('user_data.xlsx')
        sheet = wb.active

        for row in sheet.iter_rows(values_only=True):
            if row[1] == id and row[2] == password:
                return "user"  # 사용자 인증 성공

        if id == "admin" and password == "admin123":
            return "admin"  # 관리자 인증 성공

        return None  # 인증 실패

    except FileNotFoundError:
        messagebox.showerror("파일 오류", "사용자 데이터 파일을 찾을 수 없습니다.")
        return None

def perform_login():
    id = entry_username.get()
    password = entry_password.get()

    # 사용자 인증
    user_type = authenticate_user(id, password)

    if user_type == "user":
        # 사용자로 로그인한 경우 User 페이지 열기
        user_window = tk.Toplevel(root)
        user_window.title("사용자 메뉴")
        user_page = User(user_window)
        user_page.pack(fill=tk.BOTH, expand=True)
        root.withdraw()  # 로그인 윈도우 숨기기

    elif user_type == "admin":
        # 관리자로 로그인한 경우 Admin 페이지 열기
        admin_window = tk.Toplevel(root)
        admin_window.title("관리자 메뉴")
        admin_page = Admin(admin_window)
        admin_page.pack(fill=tk.BOTH, expand=True)
        root.withdraw()  # 로그인 윈도우 숨기기

    else:
        messagebox.showerror("로그인 실패", "아이디 또는 비밀번호가 일치하지 않습니다.")

# 로그인 윈도우 생성
root = tk.Tk()
root.title("로그인")

# 사용자 이름 입력 필드
label_username = tk.Label(root, text="아이디:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# 비밀번호 입력 필드
label_password = tk.Label(root, text="비밀번호:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# 로그인 버튼
login_button = tk.Button(root, text="로그인", command=perform_login)
login_button.pack()

# 프로그램 실행
root.mainloop()
