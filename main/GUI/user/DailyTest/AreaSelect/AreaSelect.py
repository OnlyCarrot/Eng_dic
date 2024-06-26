from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
import tkinter.font
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from GUI.user.DailyTest.DailyTest.DailyTest import DailyTest
from func.user.DailyTest import Daily

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AreaSelect:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(parent)
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
            180.0,
            250.0,
            image=image_image
        )
        
        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            850.0,
            200.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(
            840.0,
            300.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(
            180.0,
            240.0,
            image=image_image_3
        )

        entry_image = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(
            610.0,
            300.0,
            image=entry_image
        )

        self.entry = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry.place(
            x=480.0,
            y=170.0,
            width=260.0,
            height=60.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("TextBox-1.png"))
        entry_1 = self.canvas.create_image(
            610.0,
            200.0,
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
            x=480.0,
            y=270.0,
            width=260.0,
            height=60.0
        )

        button_image = PhotoImage(
        file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_area_select,
            relief="flat"
        )
        self.button.place(
            x = 900.0,
            y = 408.0,
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()

    def get_area_select(self):
        entered_start_num = self.entry.get()
        entered_end_num = self.entry_1.get()

        if Daily.is_digit_valid(entered_start_num) and Daily.is_digit_valid(entered_end_num):
            if int(entered_end_num) - int(entered_start_num) >= 9 and int(entered_start_num) != 0:
                Daily.save_index(entered_start_num, entered_end_num)
                self.window.withdraw()
                DailyTest(self.window)
            else:
                messagebox.showerror("비정상 범위 설정","올바른 숫자 범위가 아닙니다.")
        else:
            messagebox.showerror("숫자 입력 실패", "빈칸이거나 숫자가 아닙니다.")