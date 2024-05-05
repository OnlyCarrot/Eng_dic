import tkinter as tk
from tkinter import messagebox
import pandas as pd

def calculate_user_stats():
    # Load Excel file
    file_path = r"C:\Eng_dic\interface\OnlyCarrot\UserList.xlsx"
    try:
        df = pd.read_excel(file_path, sheet_name='usersheet')
    except FileNotFoundError:
        messagebox.showerror("에러", "파일을 찾을 수 없습니다.")
        return
    
    # Calculate average level
    average_level = df['Level'].mean()
    entry_average.delete(0, tk.END)
    entry_average.insert(0, f"{average_level:.2f}")
    
    # Find most common level
    most_common_levels = df['Level'].value_counts()
    most_common_level = most_common_levels[most_common_levels == most_common_levels.max()]
    most_common_levels_str = ", ".join([str(level) for level in most_common_level.index])
    entry_most_common.delete(0, tk.END)
    entry_most_common.insert(0, most_common_levels_str)

# Create GUI
root = tk.Tk()
root.title("사용자 통계")

label_average = tk.Label(root, text="Level 평균:")
label_average.grid(row=0, column=0, padx=10, pady=5)
entry_average = tk.Entry(root)
entry_average.grid(row=0, column=1, padx=10, pady=5)

label_most_common = tk.Label(root, text="최다 Level:")
label_most_common.grid(row=1, column=0, padx=10, pady=5)
entry_most_common = tk.Entry(root)
entry_most_common.grid(row=1, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="계산하기", command=calculate_user_stats)
button_calculate.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
