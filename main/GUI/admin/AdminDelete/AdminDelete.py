from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminDelete:
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
            130.0,
            65.0,
            image=image_image
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(
            720.0,
            270.0,
            image=image_image_1
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
            450.0,
            image=button_image_1
        )
        
        # text box
        entry_image_1 = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry_1 = self.canvas.create_image(
            715.0,
            60.0,
            image=entry_image_1,
            tags="entry"
        )

        self.canvas.tag_raise("button", "entry")  # 검색 버튼이 입력창에 가려지지 않도록 앞으로 옮기기

        self.window.resizable(False, False)
        self.window.mainloop()



if __name__ == "__main__":
    AdminDelete()
