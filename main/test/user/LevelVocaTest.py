import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from tkinter import *
from tkinter import ttk
from GUI.center_window import center_window  
from func.user.LevelVoca import LevelVoca

#Test 창 띄우기
class Test:
    def __init__(self):
        self.window = Tk()
        self.window.title("Test")
        self.window.geometry("1200x500")
        self.window.configure(bg="#FFFFFF")

        center_window(self.window, 1200, 500)

        self.canvas = Canvas(
            self.window,
            bg="#000000",
            height=500,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)   

        scroll_frame = Frame(self.canvas)
        scroll_frame.place(x=409, y=116, width=744, height=250)
        scrollbar = ttk.Scrollbar(scroll_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(scroll_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Test: 예시로 650 레벨의 단어장 표시
        levelVoca = LevelVoca()
        levelVoca.show_word(self.listbox, 650)  

        self.window.resizable(False, False)
        self.window.mainloop()

Test()