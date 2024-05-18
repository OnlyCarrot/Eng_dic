from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
import tkinter.font
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class VocaSearch:
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
        font = tkinter.font.Font(family="맑은 고딕", size=18, slant="roman")

        image_image = PhotoImage(
            file=relative_to_assets("image.png"))
        image = self.canvas.create_image(
            600.0,
            250.0,
            image=image_image
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            180.0,
            70.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(
            780.0,
            250.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("index_eng.png"))
        image_3 = self.canvas.create_image(
            470.0,
            120.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("index_kor.png"))
        image_4 = self.canvas.create_image(
            785.0,
            120.0,
            image=image_image_4
        )
        image_image_5 = PhotoImage(
            file=relative_to_assets("index_wc.png"))
        image_5 = self.canvas.create_image(
            1070.0,
            120.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_6 = self.canvas.create_image(
            790.0,
            280.0,
            image=image_image_6
        )
        # TextBox
        entry_image = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(
            800.0,
            60.0,
            image=entry_image
        )
        self.entry = Entry(
            self.canvas,
            bd=0,
            bg="#E5E5E5",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry.place(
            x=650.0,
            y=37.0,
            width=240.0,
            height=50.0
        )
        # back 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Back,
            relief="flat"
        )
        self.button.place(
            x = 700.0,
            y = 415.0,
        )
        
        # search 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.search,
            relief="flat"
        )
        self.button.place(
            x = 905.0,
            y = 40.0,
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()

    def search(self):
        messagebox.showinfo("임시","(임시)검색하기")
        
    def Back(self):
        self.window.destroy()
        self.parent.deiconify()