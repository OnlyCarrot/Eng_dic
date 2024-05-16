from pathlib import Path
from tkinter import *
import tkinter.font
from tkinter import messagebox
import sys
import os
"""
from User.mainpage import MainWindow
from Admin.admin import AdminPage
from signup import SignupPage
"""
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from GUI.center_window import center_window  # center_window 모듈 가져오기
from func.Login import login_validation

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame0"
 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Login: 
    def __init__(self):
        self.window = Tk()
        self.window.title("수준별 토익 영단어 프로그램")
        self.window.geometry("1200x500")
        self.window.configure(bg="#FFFFFF")

        center_window(self.window, 1200, 500)

        self.saved_username = "user"
        self.saved_password = "password"

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

        # entry 글자 크기 및 변수 코드
        font = tkinter.font.Font(family="맑은 고딕", size=18, slant="roman")

        # 이미지 및 위젯 생성 코드
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            600.0,
            250.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            237.0,
            221.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            232.0,
            431.0,
            image=image_image_3
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            900.0,
            250.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            905.0,
            80.0,
            image=image_image_5
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            906.0,
            229.0,
            image=image_image_7
        )

        image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            906.0,
            342.0,
            image=image_image_8
        )

        image_image_9 = PhotoImage(
            file=relative_to_assets("image-9.png"))
        image_9 = self.canvas.create_image(
            740.0,
            211.0,
            image=image_image_9
        )

        image_image_10 = PhotoImage(
            file=relative_to_assets("image-10.png"))
        image_10 = self.canvas.create_image(
            770.0,
            322.0,
            image=image_image_10
        )

        # text box
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_1.place(
            x=728.0,
            y=224.0,
            width=360.0,
            height=33.0
        )

        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font
        )
        self.entry_2.place(
            x=728.5,
            y=334.0,
            width=360.0,
            height=33.0
        )

        # Login 버튼
        button_image_1 = PhotoImage(
        file=relative_to_assets("Button.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.check_credentials,
            relief="flat"
        )
        self.button_1.place(
            x=704.0,
            y=402.0,
            width=196.0,
            height=77.0
        )

        # Sign Up 버튼
        button_image_2 = PhotoImage(
        file=relative_to_assets("Button-1.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            # command=self.signup,
            relief="flat"
        )
        self.button_2.place(
            x=924.0,
            y=402.0,
            width=196.0,
            height=77.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def check_credentials(self):
        # 입력된 사용자 이름과 비밀번호 가져오기
        entered_username = self.entry_1.get()
        entered_password = self.entry_2.get()

        
        user = login_validation(entered_username, entered_password)

        # 입력된 값과 저장된 값 비교
        if user == False:
            messagebox.showerror("로그인 실패", "사용자 이름 또는 비밀번호가 올바르지 않습니다.")
        elif user.id.startswith("ad"):
            messagebox.showinfo("로그인 성공", "관리자님, 환영합니다!")
            self.open_admin_page()
        elif user:
            messagebox.showinfo("로그인 성공", "환영합니다!")
            self.open_main_page()
            

'''
def open_main_page(self):
        MainWindow(self.window)

    def open_admin_page(self):
        self.window.withdraw()
        AdminPage(self.window)

    def signup(self):
        self.window.withdraw()
        SignupPage(self.window)
'''

if __name__ == "__main__":
    Login()
