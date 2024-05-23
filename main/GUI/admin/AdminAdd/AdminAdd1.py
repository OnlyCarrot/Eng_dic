from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window
from GUI.admin.AdminAdd.AdminAdd2 import AdminAdd2
from func.admin.VocaManage.AdminSearchVoca import word_exists, is_str_vaild

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminAdd1:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(parent)
        #self.window = Tk()
        self.window.title("수준별 토익 영단어 프로그램")
        self.window.geometry("1200x500")
        self.window.configure(bg="#FFFFFF")

        center_window(self.window, 1200, 500)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # entry 글자 크기 및 변수 코드
        font = tkinter.font.Font(family="맑은 고딕", size=24, slant="roman")

        image_image = PhotoImage(
            file=relative_to_assets("image.png"))
        image = self.canvas.create_image(
            800.0,
            100.0,
            image=image_image
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            180.0,
            250.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(
            180.0,
            230.0,
            image=image_image_2
        )

        # 중복 검사 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Next,
            relief="flat"
        )
        self.button.place(
            x = 700.0,
            y = 370.0,
        )
        
        # text box
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_1.place(
            x=560.0,
            y=170.0,
            width=480.0,
            height=65.0
        )
        

        self.window.resizable(False, False)
        self.window.mainloop()

    def Next(self):
        addWord = self.entry_1.get()
        if word_exists(addWord):
            messagebox.showerror("단어 추가 실패", "중복되지 않는 단어를 추가하세요")
        elif not is_str_vaild(addWord):
            messagebox.showerror("단어 추가 실패", "유효한 단어를 추가하세요")
        else:
            self.window.withdraw()
            AdminAdd2(self.window)