from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminDelete:
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
            130.0,
            65.0,
            image=image_image
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            720.0,
            270.0,
            image=image_image_1
        )
        
        # text box
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font,
        )
        self.entry_1.place(
            x=275.0,
            y=31.0,
            width=890.0,
            height=60.0,
        )

        # search 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            # command=
            relief="flat"
        )
        self.button.place(
            x = 1090.0,
            y = 35.0,
        )

         # back 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Back,
            relief="flat"
        )
        self.button.place(
            x = 500.0,
            y = 410.0,
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def Back(self):
        from GUI.admin.AdminMenu.AdminMenu import AdminMenu
        self.window.withdraw()
        AdminMenu(self.window)