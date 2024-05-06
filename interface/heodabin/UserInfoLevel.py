import tkinter as tk
from tkinter import messagebox
import openpyxl

class UserInfoLevel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label_title = tk.Label(self, text="사용자 레벨 조회", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.pack(pady=10)

        search_button = tk.Button(self, text="검색", command=self.show_user_level)
        search_button.pack(pady=10)

        self.level_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.level_label.pack(pady=10)

    def show_user_level(self):
        """입력된 이름으로 사용자의 레벨을 조회하여 표시하는 함수"""
        username = self.name_entry.get().strip()

        try:
            wb = openpyxl.load_workbook('user_data.xlsx')
            sheet = wb.active

            user_found = False

            for row in sheet.iter_rows(values_only=True):
                if row[0] == username:
                    user_found = True
                    level = row[3]
                    self.level_label.config(text=f"{username} 님의 레벨: {level}")
                    break

            if not user_found:
                messagebox.showwarning("조회 결과", f"'{username}' 사용자를 찾을 수 없습니다.")
                self.level_label.config(text="")

        except FileNotFoundError:
            messagebox.showerror("파일 오류", "사용자 데이터 파일을 찾을 수 없습니다.")

# 테스트 코드
if __name__ == "__main__":
    root = tk.Tk()
    root.title("사용자 레벨 조회")

    user_info_frame = UserInfoLevel(root)
    user_info_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
