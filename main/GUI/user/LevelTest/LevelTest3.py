from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
import tkinter.font
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from GUI.user.LevelTest.LevelTest4 import LevelTest4
from func.user.LevelTest import LevelTest

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LevelTest3:
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

        font = tkinter.font.Font(family="맑은 고딕", size=15, slant="roman")

        image_image = PhotoImage(
            file=relative_to_assets("image.png"))
        image = self.canvas.create_image(
            600.0,
            250.0,
            image=image_image
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(
            130.0,
            45.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_4 = self.canvas.create_image(
            130.0,
            260.0,
            image=image_image_4
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            730.0,
            250.0,
            image=image_image_1
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image-5.png"))
        image_5 = self.canvas.create_image(
            575.0,
            45.0,
            image=image_image_5
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
            y = 408.0,
        )
        
        # next 버튼
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
            x = 740.0,
            y = 408.0,
        )
        
        # TextBox
        
        entry_image_1 = PhotoImage(
            file=relative_to_assets("TextBox-1.png"))
        entry_1 = self.canvas.create_image(
            460.0,
            130.0,
            image=entry_image_1
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("TextBox-3.png"))
        entry_2 = self.canvas.create_image(
            800.0,
            130.0,
            image=entry_image_2
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("TextBox-5.png"))
        entry_4 = self.canvas.create_image(
            460.0,
            183.5,
            image=entry_image_4
        )

        
        entry_image_6 = PhotoImage(
            file=relative_to_assets("TextBox-7.png"))
        entry_6 = self.canvas.create_image(
            800.0,
            183.5,
            image=entry_image_6
        )

        
        entry_image_8 = PhotoImage(
            file=relative_to_assets("TextBox-9.png"))
        entry_8 = self.canvas.create_image(
            460.0,
            237.0,
            image=entry_image_8
        )

        
        entry_image_10 = PhotoImage(
            file=relative_to_assets("TextBox-11.png"))
        entry_10 = self.canvas.create_image(
            800.0,
            237.0,
            image=entry_image_10
        )

        
        entry_image_12 = PhotoImage(
            file=relative_to_assets("TextBox-13.png"))
        entry_12 = self.canvas.create_image(
            460.0,
            290.5,
            image=entry_image_12
        )

        
        entry_image_14 = PhotoImage(
            file=relative_to_assets("TextBox-15.png"))
        entry_14 = self.canvas.create_image(
            800.0,
            290.5,
            image=entry_image_14
        )

        
        entry_image_16 = PhotoImage(
            file=relative_to_assets("TextBox-17.png"))
        entry_16 = self.canvas.create_image(
            460.0,
            344.0,
            image=entry_image_16
        )

        
        entry_image_18 = PhotoImage(
            file=relative_to_assets("TextBox-19.png"))
        entry_18 = self.canvas.create_image(
            800.0,
            344.0,
            image=entry_image_18
        )

        self.entrys = []

        # TextBox
        for i in range(0, 5):
            self.entry = Entry(
                self.canvas,
                bd=0,
                bg="#DCDCDC",
                fg="#000716",
                highlightthickness=0,
                font=font
            )
            self.entrys.append(self.entry)
            self.entry.place(
                x=545.0,
                y=111.0 + 54.5 * i,
                width=130.0,
                height=35.0
            )
        for i in range(0, 5):
            self.entry = Entry(
                self.canvas,
                bd=0,
                bg="#DCDCDC",
                fg="#000716",
                highlightthickness=0,
                font=font
            )
            self.entrys.append(self.entry)

            self.entry.place(
                x=885.0,
                y=111.0 + 54.5 * i,
                width=130.0,
                height=35.0
            )
        index = LevelTest.show_word_meaning3(self)

        #Test
        """word = LevelTest.select_word()
        LevelTest.show_word_meaning(self, word)
        LevelTest.grade_score(" ", word)
        """
        self.window.resizable(False, False)
        self.window.mainloop()
    

    def Back(self):
        self.window.destroy()
        self.parent.deiconify()
    
    def Next(self):
        all_valid = True
        for entry in self.entrys:
            if not LevelTest.is_str_vaild(entry.get()):
                all_valid = False
                break

        if all_valid:
            self.window.withdraw
            LevelTest4(self.window)
        else:
            messagebox.showerror("제출 실패", "빈 칸이 존재하거나 잘못된 입력 형식입니다")
