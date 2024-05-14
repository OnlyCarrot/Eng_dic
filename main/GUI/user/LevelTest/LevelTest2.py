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

class LevelTest2:
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
            # command=
            relief="flat"
        )
        self.button.place(
            x = 500.0,
            y = 408.0,
        )
        
        # submit 버튼
        button_image_2 = PhotoImage(
            file=relative_to_assets("Button-2.png"))
        self.button = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            # command=
            relief="flat"
        )
        self.button.place(
            x = 740.0,
            y = 408.0,
        )
        
        # TextBox
        entry_image = PhotoImage(
            file=relative_to_assets("TextBox.png"))
        entry = self.canvas.create_image(
            610.0,
            130.0,
            image=entry_image
        )

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

        entry_image_3 = PhotoImage(
            file=relative_to_assets("TextBox-2.png"))
        entry_3 = self.canvas.create_image(
            950.0,
            130.0,
            image=entry_image_3
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("TextBox-5.png"))
        entry_4 = self.canvas.create_image(
            460.0,
            183.5,
            image=entry_image_4
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("TextBox-4.png"))
        entry_5 = self.canvas.create_image(
            610.0,
            183.5,
            image=entry_image_5
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("TextBox-7.png"))
        entry_6 = self.canvas.create_image(
            800.0,
            183.5,
            image=entry_image_6
        )

        entry_image_7 = PhotoImage(
            file=relative_to_assets("TextBox-6.png"))
        entry_7 = self.canvas.create_image(
            950.0,
            183.5,
            image=entry_image_7
        )

        entry_image_8 = PhotoImage(
            file=relative_to_assets("TextBox-9.png"))
        entry_8 = self.canvas.create_image(
            460.0,
            237.0,
            image=entry_image_8
        )

        entry_image_9 = PhotoImage(
            file=relative_to_assets("TextBox-8.png"))
        entry_9 = self.canvas.create_image(
            610.0,
            237.0,
            image=entry_image_9
        )

        entry_image_10 = PhotoImage(
            file=relative_to_assets("TextBox-11.png"))
        entry_10 = self.canvas.create_image(
            800.0,
            237.0,
            image=entry_image_10
        )

        entry_image_11 = PhotoImage(
            file=relative_to_assets("TextBox-10.png"))
        entry_11 = self.canvas.create_image(
            950.0,
            237.0,
            image=entry_image_11
        )

        entry_image_12 = PhotoImage(
            file=relative_to_assets("TextBox-13.png"))
        entry_12 = self.canvas.create_image(
            460.0,
            290.5,
            image=entry_image_12
        )

        entry_image_13 = PhotoImage(
            file=relative_to_assets("TextBox-12.png"))
        entry_13 = self.canvas.create_image(
            610.0,
            290.5,
            image=entry_image_13
        )

        entry_image_14 = PhotoImage(
            file=relative_to_assets("TextBox-15.png"))
        entry_14 = self.canvas.create_image(
            800.0,
            290.5,
            image=entry_image_14
        )

        entry_image_15 = PhotoImage(
            file=relative_to_assets("TextBox-14.png"))
        entry_15 = self.canvas.create_image(
            950.0,
            290.5,
            image=entry_image_15
        )

        entry_image_16 = PhotoImage(
            file=relative_to_assets("TextBox-17.png"))
        entry_16 = self.canvas.create_image(
            460.0,
            344.0,
            image=entry_image_16
        )

        entry_image_17 = PhotoImage(
            file=relative_to_assets("TextBox-16.png"))
        entry_17 = self.canvas.create_image(
            610.0,
            344.0,
            image=entry_image_17
        )

        entry_image_18 = PhotoImage(
            file=relative_to_assets("TextBox-19.png"))
        entry_18 = self.canvas.create_image(
            800.0,
            344.0,
            image=entry_image_18
        )

        entry_image_19 = PhotoImage(
            file=relative_to_assets("TextBox-18.png"))
        entry_19 = self.canvas.create_image(
            950.0,
            344.0,
            image=entry_image_19
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()



if __name__ == "__main__":
    LevelTest2()
