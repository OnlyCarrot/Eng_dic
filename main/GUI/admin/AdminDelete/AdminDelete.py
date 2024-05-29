from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font
import tkinter as tk
from tkinter import ttk
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window
from func.admin.VocaManage.DeleteVoca import DeleteVoca
from func.user.Voca import Voca

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminDelete:
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

        # 스크롤바 프레임 생성
        scroll_frame = Frame(self.canvas)
        scroll_frame.place(x=277, y=154, width=890, height=250)
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
            width=890.0,
            height=60.0,
        )

        self.entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font,
        )
        self.entry_2.place(
            x=40.0,
            y=220.0,
            width=195.0,
            height=48.0,
        )

        # search 버튼
        button_image = PhotoImage(
            file=relative_to_assets("Button.png"))
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.search,
            relief="flat"
        )
        self.button.place(
            x = 1090.0,
            y = 35.0,
        )

        # delete 버튼
        button_image_2 = PhotoImage(
            file=relative_to_assets("Button-2.png"))
        self.button = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete,
            relief="flat"
        )
        self.button.place(
            x = 35.0,
            y = 310.0,
        )
    
         # back 버튼
        button_image_1 = PhotoImage(
            file=relative_to_assets("Button-1.png"))
        self.button = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Back,
            relief="flat"
        )
        self.button.place(
            x = 500.0,
            y = 410.0,
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def search(self):
        self.listbox.delete(0, tk.END)
        delete_word_list = self.entry_1.get()
        deleteVoca = DeleteVoca()

        voca = Voca()
        word_list = voca.search_voca(delete_word_list)
        for word in word_list:
            eng_kor_c = f"{word[0]}-{word[1]}-{word[2]}"
            self.listbox.insert(tk.END, eng_kor_c)

    def Back(self):
        from GUI.admin.AdminMenu.AdminMenu import AdminMenu
        self.window.withdraw()
        AdminMenu(self.window)

    def delete(self):
        entered_delete_word = self.entry_2.get()
        deleteVoca = DeleteVoca()
        if deleteVoca.is_str_valid(entered_delete_word):
            deleteVoca.delete_word(entered_delete_word)
            messagebox.showinfo("삭제 성공", "성공적으로 단어가 삭제되었습니다.")
        else:
            messagebox.showerror("단어 삭제 실패", "형식이 유효하지 않거나, 존재하지 않는 단어입니다.")