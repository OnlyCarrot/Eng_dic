from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font 
import os
import sys
import tkinter as tk
from tkinter import ttk



sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window
from GUI.admin.AdminModify.AdminModify2 import AdminModify2
# from func.admin.VocaManage.ModifyVoca import is_str_valid
# from main.func.admin.VocaManage.AdminSearchVoca import word_exists

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminModify1:

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

        # entry 글자 크기 및 변수 코드
        font = tkinter.font.Font(family="맑은 고딕", size=24, slant="roman")

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

         # 스크롤바 프레임 생성
        scroll_frame = Frame(self.canvas)
        scroll_frame.place(x=275, y=145, width=890, height=250)
        # 스크롤바 생성
        scrollbar = ttk.Scrollbar(scroll_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # 리스트박스 생성
        self.listbox = Listbox(scroll_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        # text box
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font,
            
        )
        self.entry_1.place(
            x=275.0,
            y=31.0,
            width= 890.0,
            height=60.0,
        )

        # back 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Back,
            relief="flat"
        )
        self.button.place(
            x = 550.0,
            y = 410.0,
        )

        # search 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.search,
            relief="flat"
        )
        self.button.place(
            x = 1090.0,
            y = 35.0,
        )

        self.window.resizable(False, False)
        self.window.mainloop()
    
    def search(self):
        from main.func.admin.VocaManage.ModifyVoca import is_str_valid
        from func.user.Voca import Voca
        from func.admin.VocaManage.AdminSearchVoca import word_exists
        self.listbox.delete(0, tk.END)
        modify_word = self.entry_1.get()
        if not is_str_valid(modify_word):
            messagebox.showerror("단어 수정 실패", "유효한 형식으로 입력하세요")
        else:
            voca = Voca()
            word_list = voca.search_voca(modify_word)
            for word in word_list:
                eng_kor_c = f"{word[0]}-{word[1]}-{word[2]}"
                self.listbox.insert(tk.END, eng_kor_c)
            if word_exists(modify_word):
                self.window.withdraw()
                AdminModify2(self.window, modify_word)
                return modify_word
            else:
                messagebox.showerror("단어 수정 실패", "정확한 단어를 입력해주세요")
            

    # edit 버튼이 생길 시에 동작할 AdminModify2화면으로 이동하는 함수
    def Next(self):
        self.window.withdraw()
        AdminModify2(self.window)

    def Back(self):
        from GUI.admin.AdminMenu.AdminMenu import AdminMenu
        self.window.withdraw()
        AdminMenu(self.window)



        
        