from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
import tkinter.font
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from GUI.user.LevelTest.LevelTest1 import LevelTest1
from func.user.SignUp import sign_up
from func.UserDBManager import UserDBManager
from func.user.SignUp import is_str_vaild, is_pw_dupli

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SignUp:
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

        font = tkinter.font.Font(family="맑은 고딕", size=13, slant="roman")

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
            237.0,
            221.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(
            254.0,
            431.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(
            900.0,
            250.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_4 = self.canvas.create_image(
            750.0,
            80.0,
            image=image_image_4
        )
        # 입력칸
        entry_image_1 = PhotoImage(
            file=relative_to_assets("Group-2.png"))
        entry_1 = self.canvas.create_image(
            908.0,
            145,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_1.place(
            x=727.0,
            y=142.0,
            width=363.0,
            height=26.0
        )
        entry_image_2 = PhotoImage(
            file=relative_to_assets("Group-3.png"))
        entry_2 = self.canvas.create_image(
            908.0,
            216,
            image=entry_image_2
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
            x=727.0,
            y=213.0,
            width=363.0,
            height=26.0
        )
        entry_image_3 = PhotoImage(
            file=relative_to_assets("Group-4.png"))
        entry_3 = self.canvas.create_image(
            908.0,
            287,
            image=entry_image_3
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
            x=727.0,
            y=283.0,
            width=363.0,
            height=26.0
        )
        entry_image_4 = PhotoImage(
            file=relative_to_assets("Group-5.png"))
        entry_4 = self.canvas.create_image(
            908.0,
            358,
            image=entry_image_4
        )
        self.entry_4 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_4.place(
            x=727.0,
            y=354.0,
            width=363.0,
            height=26.0
        )
        # login 버튼
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
            x=710.0,
            y=400.0,
            width=196.0,
            height=77.0
        )
        # next 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.temp1,
            relief="flat"
        )
        self.button_1.place(
            x=920.0,
            y=400.0,
            width=196.0,
            height=77.0
        )

        #Test
        #sign_up("S", "ss", "sss", "ssss", 4)

        self.window.resizable(False, False)
        self.window.mainloop()
        
    def temp1(self):
        EnteredId = self.entry_1.get()
        EnteredUsername = self.entry_2.get()
        EnteredPw1 = self.entry_3.get()
        EnteredPw2 = self.entry_4.get()

        entries = [EnteredId, EnteredUsername, EnteredPw1, EnteredPw2]
        
        ub = UserDBManager()
        if ub.user_exists(EnteredId):   
            messagebox.showerror("ID 중복", "중복되는 ID입니다!")
        elif not is_str_vaild(entries):
            messagebox.showerror("회원가입 실패", "빈 칸이 존재합니다")
        elif is_pw_dupli(EnteredPw1, EnteredPw2):
            messagebox.showerror("회원가입 실패", "비밀번호가 일치하지 않습니다")
        else:
            templist = []
            templist.append(EnteredId)
            templist.append(EnteredUsername)
            templist.append(EnteredPw1)
            templist.append(EnteredPw2)
            self.window.withdraw()
            LevelTest1(self.window)

    def Back(self):
        self.window.destroy()
        self.parent.deiconify()