from pathlib import Path
from tkinter import *
from tkinter import messagebox
"""
from User.mainpage import MainWindow
from Admin.admin import AdminPage
from signup import SignupPage
"""
from center_window import center_window  # center_window 모듈 가져오기

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminUserInfo2:
    def __init__(self):
        self.window = Tk()
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
            280.0,
            image=image_image
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_5 = self.canvas.create_image(
            130.0,
            60.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image-5.png"))
        image_5 = self.canvas.create_image(
            330.0,
            250.0,
            image=image_image_5
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image-6.png"))
        image_6 = self.canvas.create_image(
            800.0,
            280.0,
            image=image_image_6
        )

         # TextBox
        entry_image = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(
            700.0,
            65.0,
            image=entry_image
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("TextBox-6.png"))
        entry_6 = self.canvas.create_image(
            330.0,
            396.0,
            image=entry_image_6
        )

        # search 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        temp = self.canvas.create_image(
            1125.0,
            60.0,
            image=button_image,
            tags="button"
        )

        # back 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        temp_1 = self.canvas.create_image(
            600.0,
            465.0,
            image=button_image_1
        )

        # self.canvas.tag_raise("button", "entry")  # 검색 버튼이 입력창에 가려지지 않도록 앞으로 옮기기

        self.window.resizable(True, True)
        self.window.mainloop()



if __name__ == "__main__":
    AdminUserInfo2()
