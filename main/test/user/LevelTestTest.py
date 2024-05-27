import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.user.LevelTest import LevelTest
from tkinter import *
from GUI.center_window import center_window  

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

        #Test: 단어 제대로 찍히는지 확인
        LevelTest.show_word_meaning2(self)

        self.window.resizable(False, False)
        self.window.mainloop()

Test()

