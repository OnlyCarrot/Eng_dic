import tkinter as tk
from tkinter import messagebox
import pandas as pd

def check_user_level():
    # Get user input
    user_id = entry_id.get()
    user_name = entry_name.get()
    
    # Check if either ID or Name is provided
    if not user_id and not user_name:
        messagebox.showwarning("경고", "ID나 이름 중 하나를 입력하세요.")
        return
    
    # Load Excel file
    file_path = r"C:\Eng_dic\interface\OnlyCarrot\UserList.xlsx"
    try:
        df = pd.read_excel(file_path, sheet_name='usersheet')
    except FileNotFoundError:
        messagebox.showerror("에러", "파일을 찾을 수 없습니다.")
        return
    
    # Check if user exists
    if user_id:
        user_info = df[df['ID'] == user_id]
    else:
        user_info = df[df['Name'] == user_name]
    
    if user_info.empty:
        messagebox.showwarning("경고", "해당 사용자가 존재하지 않습니다.")
    else:
        user_level = user_info.iloc[0]['Level']
        messagebox.showinfo("사용자 등급", f"{user_id if user_id else user_name}의 등급은 {user_level} 입니다.")

# Create GUI
root = tk.Tk()
root.title("사용자 등급 확인")

label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

button_check = tk.Button(root, text="확인하기", command=check_user_level)
button_check.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
