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

class LevelVoca:
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
            180.0,
            68.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image-3.png"))
        image_2 = self.canvas.create_image(
            780.0,
            250.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image-4.png"))
        image_2 = self.canvas.create_image(
            780.0,
            240.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("index_num.png"))
        image_4 = self.canvas.create_image(
            520.0,
            92.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("index_eng.png"))
        image_5 = self.canvas.create_image(
            691.0,
            92.0,
            image=image_image_5
        )
        
        image_image_6 = PhotoImage(
            file=relative_to_assets("index_kor.png"))
        image_6 = self.canvas.create_image(
            862.0,
            92.0,
            image=image_image_6
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("index_wc.png"))
        image_7 = self.canvas.create_image(
            1075.0,
            92.0,
            image=image_image_7
        )

        # back 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        temp = self.canvas.create_image(
            790.0,
            450.0,
            image=button_image
        )

        self.window.resizable(True, True)
        self.window.mainloop()



if __name__ == "__main__":
    LevelVoca()
