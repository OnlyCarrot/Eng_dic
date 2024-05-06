import tkinter as tk
from tkinter import messagebox
import random

class NumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("숫자 게임")
        
        # 숫자 리스트 생성
        self.number_list = list(range(1, 6))
        random.shuffle(self.number_list)
        
        # 현재 숫자 표시 라벨
        self.current_number_label = tk.Label(root, text="현재 숫자: ")
        self.current_number_label.pack()
        
        # 현재 숫자 출력
        self.current_number_var = tk.StringVar()
        self.current_number_var.set(str(self.number_list[0]))
        self.current_number_display = tk.Label(root, textvariable=self.current_number_var, font=("Helvetica", 24))
        self.current_number_display.pack()
        
        # 사용자 입력 창
        self.user_input_entry = tk.Entry(root)
        self.user_input_entry.pack()
        
        # 확인 버튼
        self.confirm_button = tk.Button(root, text="확인", command=self.check_number)
        self.confirm_button.pack()
        
        # 초기화 버튼
        self.reset_button = tk.Button(root, text="초기화", command=self.reset_game)
        self.reset_button.pack()
        
        # 현재 인덱스
        self.current_index = 0
        self.success_count = 0
        self.fail_count = 0

    def check_number(self):
        try:
            user_input = int(self.user_input_entry.get())
            current_number = int(self.current_number_var.get())
            if user_input > current_number:
                self.success_count += 1
                self.next_number()
            elif user_input == current_number:
                self.success_count += 1
                self.next_number()
            else:
                self.fail_count += 1
                self.next_number()
        except ValueError:
            pass

    def next_number(self):
        self.current_index += 1
        if self.current_index < len(self.number_list):
            self.current_number_var.set(str(self.number_list[self.current_index]))
            self.user_input_entry.delete(0, tk.END)
        else:
            self.show_result()

    def reset_game(self):
        self.current_index = 0
        random.shuffle(self.number_list)
        self.current_number_var.set(str(self.number_list[0]))
        self.user_input_entry.delete(0, tk.END)
        self.success_count = 0
        self.fail_count = 0

    def show_result(self):
        messagebox.showinfo("게임 결과", f"성공: {self.success_count}개, 실패: {self.fail_count}개")

# Tkinter 애플리케이션 시작
root = tk.Tk()
app = NumberGame(root)
root.mainloop()
