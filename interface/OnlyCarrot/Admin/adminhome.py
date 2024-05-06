import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("단어 관리 프로그램")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        # 첫 번째 열의 버튼
        btn_add_word = tk.Button(self, text="단어 추가", command=self.add_word)
        btn_add_word.grid(row=0, column=0, padx=10, pady=5)

        btn_delete_word = tk.Button(self, text="단어 삭제", command=self.delete_word)
        btn_delete_word.grid(row=1, column=0, padx=10, pady=5)

        btn_modify_word = tk.Button(self, text="단어 수정", command=self.modify_word)
        btn_modify_word.grid(row=2, column=0, padx=10, pady=5)

        # 두 번째 열의 버튼
        btn_word_distribution = tk.Button(self, text="등급 분포", command=self.word_distribution)
        btn_word_distribution.grid(row=0, column=1, padx=10, pady=5)

        btn_member_grade = tk.Button(self, text="회원별 등급", command=self.member_grade)
        btn_member_grade.grid(row=1, column=1, padx=10, pady=5)

    def add_word(self):
        # ToDo: 단어 추가 기능 구현
        pass

    def delete_word(self):
        # ToDo: 단어 삭제 기능 구현
        pass

    def modify_word(self):
        # ToDo: 단어 수정 기능 구현
        pass

    def word_distribution(self):
        # ToDo: 등급 분포 확인 기능 구현
        pass

    def member_grade(self):
        # ToDo: 회원별 등급 확인 기능 구현
        pass

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
