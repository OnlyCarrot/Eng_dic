from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class UserMenu:
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
        temp = self.canvas.create_image(
            908.0,
            105.0,
            image=button_image
        )
        # 수준별 단어 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        temp_1 = self.canvas.create_image(
            908.0,
            201.0,
            image=button_image_1
        )
        # 일일 테스트 버튼
        button_image_2 = PhotoImage(
            file=relative_to_assets("Button-2.png"))
        temp_2 = self.canvas.create_image(
            908.0,
            297.0,
            image=button_image_2
        )

        # logout 버튼
        button_image_3 = PhotoImage(
            file=relative_to_assets("Button-3.png"))
        temp_3 = self.canvas.create_image(
            806.0,
            440.0,
            image=button_image_3
        )
        # quit program 버튼
        button_image_4 = PhotoImage(
            file=relative_to_assets("Button-4.png"))
        temp_4 = self.canvas.create_image(
            1026.0,
            440.0,
            image=button_image_4
        )

        self.window.resizable(True, True)
        self.window.mainloop()



if __name__ == "__main__":
    UserMenu()
