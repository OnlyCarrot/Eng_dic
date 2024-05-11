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

class AdminUserInfo1:
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

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-2.png"))
        image_4 = self.canvas.create_image(
            300.0,
            280.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_1 = self.canvas.create_image(
            755.0,
            280.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_5 = self.canvas.create_image(
            130.0,
            60.0,
            image=image_image_4
        )

         # TextBox
        entry_image = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(
            700.0,
            65.0,
            image=entry_image
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("TextBox-1.png"))
        entry_1 = self.canvas.create_image(
            515.0,
            285.0,
            image=entry_image_1
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("TextBox-2.png"))
        entry_2 = self.canvas.create_image(
            900.0,
            175.0,
            image=entry_image_2
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("TextBox-3.png"))
        entry_3 = self.canvas.create_image(
            900.0,
            247.0,
            image=entry_image_3
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("TextBox-4.png"))
        entry_4 = self.canvas.create_image(
            900.0,
            320.0,
            image=entry_image_4
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("TextBox-5.png"))
        entry_5 = self.canvas.create_image(
            900.0,
            390.0,
            image=entry_image_5
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
    AdminUserInfo1()
