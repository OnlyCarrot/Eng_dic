from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from GUI.user.VocaSearch.VocaSearch import VocaSearch
from GUI.user.LevelVoca.LevelVoca import LevelVoca
from GUI.user.DailyTest.AreaSelect.AreaSelect import AreaSelect
from func.user.DailyTest import Daily
from func.User import User
from datetime import date


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class UserMenu:
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
        # 단어장 조회 및 검색 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.VocaSearch,
            relief="flat"
        )
        self.button.place(
            x = 700.0,
            y = 70.0,
        )

        # 수준별 단어 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.LevelVoca,
            relief="flat"
        )
        self.button.place(
            x = 700.0,
            y = 170.0,
        )
        
        # 일일 테스트 버튼
        button_image_2 = PhotoImage(
            file=relative_to_assets("Button-2.png"))
        self.button = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.DailyTest,
            relief="flat"
        )
        self.button.place(
            x = 700.0,
            y = 270.0,
        )

        # logout 버튼
        button_image_3 = PhotoImage(
            file=relative_to_assets("Button-3.png"))
        self.button = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Logout,
            relief="flat"
        )
        self.button.place(
            x = 710.0,
            y = 400.0,
        )
        
        # quit program 버튼
        button_image_4 = PhotoImage(
            file=relative_to_assets("Button-4.png"))
        self.button = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.Quit,
            relief="flat"
        )
        self.button.place(
            x = 920.0,
            y = 400.0,
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()
    """
    단순 화면 전환만 적용했습니다. 부가 기능은 추후에 더할 예정.
    """
    def VocaSearch(self):
        self.window.withdraw()
        VocaSearch(self.window)

    def LevelVoca(self):
        self.window.withdraw()
        LevelVoca(self.window)

    def DailyTest(self):
        user = User()
        last_test_date = user.get_last_test_date()
        last_test_date = last_test_date.strftime("%Y-%m-%d")
        today = date.today().strftime("%Y-%m-%d")
        if last_test_date == today:
            messagebox.showinfo("오류", "오늘은 이미 일일테스트를 수행하셨습니다.")
            return
        else:
            self.window.withdraw()
            AreaSelect(self.window)

    def Quit(self):
        self.window.destroy()
        sys.exit()

    def Logout(self):
        from GUI.Login.Login import Login
        self.window.withdraw()
        Login(self.window)