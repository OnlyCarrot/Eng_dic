import tkinter as tk

def center_window(window, width, height):
    # 화면의 너비와 높이를 가져옴
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 창의 위치를 계산하여 화면의 중앙에 위치하도록 설정
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
