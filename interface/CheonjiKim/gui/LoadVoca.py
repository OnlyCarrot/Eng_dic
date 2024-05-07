import tkinter as tk
from tkinter import messagebox


#버튼마다 적절하게 함수를 직접 구현해야 한다.
def callback():
    pass

root = tk.Tk()
root.title("English Vocabulary")

# Create labels and entry fields for using voca

search_button = tk.Button(root, text="단어 검색", command=lambda: callback())
search_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

loadall_button = tk.Button(root, text="전체 단어 조회", command=lambda: callback())
loadall_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

loadall_button = tk.Button(root, text="수준별 단어 조회", command=lambda: callback())
loadall_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

daily_test_buttom = tk.Button(root, text="일일 테스트", command=lambda: callback())
daily_test_buttom.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()

