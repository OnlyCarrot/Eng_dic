import tkinter as tk
from tkinter import messagebox
import openpyxl
import matplotlib.pyplot as plt

class UserInfoDistri(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        label_title = tk.Label(self, text="사용자 레벨 분포", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        # 사용자 레벨 데이터를 저장할 딕셔너리
        self.level_distribution = {1: 0, 2: 0, 3: 0}

        try:
            wb = openpyxl.load_workbook('user_data.xlsx')
            sheet = wb.active

            for row in sheet.iter_rows(values_only=True):
                level = row[3]
                if level in self.level_distribution:
                    self.level_distribution[level] += 1

            # 차트 그리기
            self.plot_distribution()

        except FileNotFoundError:
            messagebox.showerror("파일 오류", "사용자 데이터 파일을 찾을 수 없습니다.")

    def plot_distribution(self):
        """사용자 레벨 분포를 차트로 시각화하는 함수"""
        levels = list(self.level_distribution.keys())
        counts = list(self.level_distribution.values())

        # 파이 차트 그리기
        plt.figure(figsize=(8, 6))
        plt.pie(counts, labels=levels, autopct='%1.1f%%', startangle=140)
        plt.title("사용자 레벨 분포")
        plt.axis('equal')  # 원형 차트로 설정
        plt.show()

# 테스트 코드
if __name__ == "__main__":
    root = tk.Tk()
    root.title("사용자 레벨 분포")

    user_info_frame = UserInfoDistri(root)
    user_info_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
