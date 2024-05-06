import tkinter as tk
from tkinter import messagebox
import openpyxl
from LevelTest import LevelTest # type: ignore

def save_to_excel(name, username, password):
    # 엑셀 파일 경로 지정 (원하는 경로로 수정하세요)
    excel_file = 'user_data.xlsx'

    try:
        # 엑셀 파일 열기 (없으면 새로 생성)
        wb = openpyxl.load_workbook(excel_file)
    except FileNotFoundError:
        # 파일이 없는 경우 새로운 워크북 생성
        wb = openpyxl.Workbook()

    # 첫 번째 시트 선택 (기본적으로 생성된 시트 사용)
    sheet = wb.active

    # 새로운 사용자 데이터를 엑셀 시트에 추가
    new_row = [name, username, password]
    sheet.append(new_row)

    # 변경 내용을 파일에 저장
    wb.save(excel_file)

    messagebox.showinfo("회원가입 성공", "회원가입이 완료되었습니다!")

def register_user():
    name = entry_name.get()
    username = entry_username.get()
    password = entry_password.get()
    password_confirm = entry_password_confirm.get()

    if not name or not username or not password or not password_confirm:
        messagebox.showerror("입력 오류", "모든 필드를 입력해주세요.")
        return

    if password != password_confirm:
        messagebox.showerror("입력 오류", "비밀번호가 일치하지 않습니다.")
        return

    save_to_excel(name, username, password)
    execute_level_test(username)

def execute_level_test(username):
    try:
        level_test_gui = LevelTest(username)
        level_test_gui.mainloop()
    except Exception as e:
        messagebox.showerror("오류", f"LevelTest 실행 중 오류 발생: {e}")

# 메인 윈도우 생성
root = tk.Tk()
root.title("회원가입")

# 이름 입력 필드
label_name = tk.Label(root, text="이름:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

# 아이디 입력 필드
label_username = tk.Label(root, text="아이디:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# 비밀번호 입력 필드
label_password = tk.Label(root, text="비밀번호:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# 비밀번호 확인 입력 필드
label_password_confirm = tk.Label(root, text="비밀번호 확인:")
label_password_confirm.pack()
entry_password_confirm = tk.Entry(root, show="*")
entry_password_confirm.pack()

# 회원가입 버튼
register_button = tk.Button(root, text="회원가입", command=register_user)
register_button.pack()

# 프로그램 실행
root.mainloop()
