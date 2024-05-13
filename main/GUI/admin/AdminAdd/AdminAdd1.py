from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys

from GUI.center_window import center_window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AdminAdd1:
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
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        image_image = PhotoImage(file=relative_to_assets("image.png"))
        image = self.canvas.create_image(800.0, 100.0, image=image_image)

        image_image_1 = PhotoImage(file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(180.0, 250.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(180.0, 230.0, image=image_image_2)

        # 중복 검사 버튼
        button_image = PhotoImage(file=relative_to_assets("Button.png"))
        temp = self.canvas.create_image(800.0, 400.0, image=button_image)

        # text box
        entry_image = PhotoImage(file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(800.0, 200.0, image=entry_image)

        self.window.resizable(False, False)
        self.window.mainloop()


if __name__ == "__main__":
    AdminAdd1()
