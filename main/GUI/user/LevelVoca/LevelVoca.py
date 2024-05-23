from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from func.user.LevelVoca import LevelVoca as lv
from func.User import User


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LevelVoca:
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
            68.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_2 = self.canvas.create_image(
            780.0,
            250.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_2 = self.canvas.create_image(
            780.0,
            240.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("index_num.png"))
        image_4 = self.canvas.create_image(
            520.0,
            92.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("index_eng.png"))
        image_5 = self.canvas.create_image(
            691.0,
            92.0,
            image=image_image_5
        )
        
        image_image_6 = PhotoImage(
            file=relative_to_assets("index_kor.png"))
        image_6 = self.canvas.create_image(
            862.0,
            92.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("index_wc.png"))
        image_7 = self.canvas.create_image(
            1075.0,
            92.0,
            image=image_image_7
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
            y = 400.0,
        )

        # 스크롤바 프레임 생성
        scroll_frame = Frame(self.canvas)
        scroll_frame.place(x=409, y=116, width=744, height=250)

        # 스크롤바 생성
        scrollbar = ttk.Scrollbar(scroll_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # 리스트박스 생성
        self.listbox = Listbox(scroll_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        # 스크롤바와 리스트박스 연결
        scrollbar.config(command=self.listbox.yview)

        levelVoca = lv()
        user = User()
        levelVoca.show_word(self.listbox, user.get_level())  # 예시로 650 레벨의 단어장 표시

        self.window.resizable(False, False)
        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        self.parent.deiconify()