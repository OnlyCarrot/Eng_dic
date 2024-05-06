import tkinter as tk
from tkinter import ttk
import openpyxl

class VocaShow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("단어 전체 보기")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # 엑셀 파일에서 단어 데이터 읽기
        words, meanings = self.load_word_data()

        # 단어 데이터를 표시할 Treeview 생성
        self.tree = ttk.Treeview(self, columns=("Word", "Meaning"), show="headings")
        self.tree.heading("Word", text="영어 단어")
        self.tree.heading("Meaning", text="한글 뜻")

        # 표에 단어 데이터 추가
        for word, meaning in zip(words, meanings):
            self.tree.insert("", "end", values=(word, meaning))

        self.tree.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    def load_word_data(self):
        words = []
        meanings = []

        try:
            wb = openpyxl.load_workbook('word_data.xlsx')
            sheet = wb.active

            for row in sheet.iter_rows(values_only=True):
                words.append(row[0])
                meanings.append(row[1])

            return words, meanings

        except FileNotFoundError:
            tk.messagebox.showerror("파일 오류", "단어 데이터 파일을 찾을 수 없습니다.")
            return [], []

# 사용 예시
if __name__ == "__main__":
    root = tk.Tk()
    root.title("VocaShow 사용 예시")

    voca_show = VocaShow(root)
    voca_show.mainloop()
