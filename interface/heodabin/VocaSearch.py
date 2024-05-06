import tkinter as tk
from tkinter import messagebox
import openpyxl

class VocaSearch(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.word_data = self.load_word_data()

        label_title = tk.Label(self, text="단어 검색", font=("Helvetica", 16, "bold"))
        label_title.pack(pady=20)

        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.pack(pady=10)

        search_button = tk.Button(self, text="검색", command=self.search_word)
        search_button.pack(pady=10)

        self.result_text = tk.Text(self, height=10, width=40, wrap=tk.WORD)
        self.result_text.pack(pady=20)

    def load_word_data(self):
        """word_data를 엑셀 파일에서 읽어오는 함수"""
        word_data = []

        try:
            wb = openpyxl.load_workbook('word_data.xlsx')
            sheet = wb.active

            for row in sheet.iter_rows(values_only=True):
                word_data.append((row[0], row[1]))  # (영어단어, 한글뜻) 튜플 형태로 저장

        except FileNotFoundError:
            messagebox.showerror("파일 오류", "단어 데이터 파일을 찾을 수 없습니다.")

        return word_data

    def search_word(self):
        """단어 검색을 수행하고 결과를 출력하는 함수"""
        search_term = self.search_entry.get().strip().lower()
        self.result_text.delete(1.0, tk.END)  # 결과 텍스트 초기화

        if not search_term:
            messagebox.showwarning("검색 오류", "검색어를 입력하세요.")
            return

        search_results = []
        for word, meaning in self.word_data:
            if search_term in word.lower() or search_term in meaning.lower():
                search_results.append((word, meaning))

        if search_results:
            self.display_search_results(search_results)
        else:
            self.result_text.insert(tk.END, "검색 결과가 없습니다.")

    def display_search_results(self, results):
        """검색 결과를 텍스트 위젯에 출력하는 함수"""
        for word, meaning in results:
            self.result_text.insert(tk.END, f"{word}: {meaning}\n")

# 테스트 코드
if __name__ == "__main__":
    root = tk.Tk()
    root.title("단어 검색")

    search_frame = VocaSearch(root)
    search_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
