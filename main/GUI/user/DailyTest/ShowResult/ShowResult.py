from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from GUI.user.DailyTest.DailyTest import DailyTest
from func.user.DailyTest import Daily
from func.User import User

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ShowResult:
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
            730.0,
            250.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(
            130.0,
            45.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(
            130.0,
            140.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_4 = self.canvas.create_image(
            360.0,
            45.0,
            image=image_image_4
        )
        # done 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Done,
            relief="flat"
        )
        self.button.place(
            x = 650.0,
            y = 408.0,
        )
        
        # 점수별 이미지 출력
        image_image_5 = PhotoImage(
            file=relative_to_assets(f"i{DailyTest.score}.png"))
        image_5 = self.canvas.create_image(
            630.0,
            230.0,
            image=image_image_5
        )
        
        # ToDo
        # Daily.change_level(User.get_level(), DailyTest.score)
        self.window.resizable(False, False)
        self.window.mainloop()

    def Done(self):
        from GUI.user.UserMenu.UserMenu import UserMenu
        user = User()
        Daily.update_user(DailyTest.score, user)
        self.window.withdraw()
        UserMenu(self.window)
    