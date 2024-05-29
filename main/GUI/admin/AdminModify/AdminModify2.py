from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font
import os
import sys




sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminModify2:
    def __init__(self, parent, modify_word):
        self.parent = parent
        self.modify_word = modify_word
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

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-6.png"))
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

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(
            930.0,
            310.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_4 = self.canvas.create_image(
            930.0,
            210.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image-5.png"))
        image_5 = self.canvas.create_image(
            930.0,
            110.0,
            image=image_image_5
        )

        # edit 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button-2.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Modify_then_Back,
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
            x=578.0,
            y=80.0,
            width=270.0,
            height=62.0
        )

        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_2.place(
            x=578.0,
            y=180.0,
            width=270.0,
            height=62.0
        )

        self.entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_3.place(
            x=578.0,
            y=280.0,
            width=270.0,
            height=62.0
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()

    def Back(self):
        from GUI.admin.AdminMenu.AdminMenu import AdminMenu
        self.window.withdraw()
        AdminMenu(self.window)

    def Modify_then_Back(self):
        #Modify 기능 실행
        from func.admin.VocaManage.ModifyVoca import edit_word
        from main.func.admin.VocaManage.AdminSearchVoca import word_exists
        modify_eng = self.entry_1.get()
        modify_kor = self.entry_2.get()
        modify_wc = self.entry_3.get()
        edit_word(self.modify_word, modify_eng, modify_kor, modify_wc)

        # 뒤로가기 기능 실행
        self.Back()
