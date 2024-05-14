from pathlib import Path
from tkinter import *
from tkinter import messagebox
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../..")
from GUI.center_window import center_window  # center_window 모듈 가져오기
from func.user.SignUp import sign_up


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class SignUp:
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
        image = self.canvas.create_image(600.0, 250.0, image=image_image)

        image_image_1 = PhotoImage(file=relative_to_assets("image-1.png"))
        image_1 = self.canvas.create_image(237.0, 221.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image-2.png"))
        image_2 = self.canvas.create_image(254.0, 431.0, image=image_image_2)

        image_image_3 = PhotoImage(file=relative_to_assets("image-3.png"))
        image_3 = self.canvas.create_image(900.0, 250.0, image=image_image_3)

        image_image_4 = PhotoImage(file=relative_to_assets("image-4.png"))
        image_4 = self.canvas.create_image(750.0, 80.0, image=image_image_4)
        # 입력칸
        entry_image_1 = PhotoImage(file=relative_to_assets("Group-2.png"))
        entry_1 = self.canvas.create_image(908.0, 145, image=entry_image_1)

        entry_image_2 = PhotoImage(file=relative_to_assets("Group-3.png"))
        entry_2 = self.canvas.create_image(908.0, 216, image=entry_image_2)

        entry_image_3 = PhotoImage(file=relative_to_assets("Group-4.png"))
        entry_3 = self.canvas.create_image(908.0, 287, image=entry_image_3)

        entry_image_4 = PhotoImage(file=relative_to_assets("Group-5.png"))
        entry_4 = self.canvas.create_image(908.0, 358, image=entry_image_4)
        # login 버튼
        button_image = PhotoImage(file=relative_to_assets("Button.png"))
        temp = self.canvas.create_image(810.0, 434.0, image=button_image)
        # next 버튼
        button_image_1 = PhotoImage(file=relative_to_assets("Button-1.png"))
        temp_1 = self.canvas.create_image(1025.0, 434.0, image=button_image_1)

<<<<<<< HEAD
        # signUpTest id, username, password, role, level
        sign_up("s", "ss", "sss", "user", 4)

=======
>>>>>>> 1bd22a4 (all fix done!)
        self.window.resizable(False, False)
        self.window.mainloop()


if __name__ == "__main__":
    SignUp()
