from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter.font
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../../..')
from GUI.center_window import center_window
from GUI.admin.AdminUserInfo.AdminUserInfo2 import AdminUserInfo2
from func.UserDBManager import UserDBManager
from func.admin.VocaManage.AdminSearchVoca import process_str
from func.admin.UserManage.RoadUserInfo import is_str_valid

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame"
glo_user_info1 = []

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AdminUserInfo1:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(parent)
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
        self.entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=font,
            
        )
        self.entry_1.place(
            x=255.0,
            y=31.0,
            width= 900.0,
            height=60.0,
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
        self.button = Button(
            self.canvas,
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.Next,
            relief="flat"
        )
        self.button.place(
            x = 1090.0,
            y = 35.0,
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
            y = 433.0,
        )

        # 총 회원 수 화면에 쏘기
        user_manager = UserDBManager()
        all_user_records = user_manager.get_all_user_records()
        user_num = len(all_user_records)
        font = tkinter.font.Font(family="맑은 고딕", size=18, slant="roman")
        self.canvas.create_text(505.0, 288.0, text=user_num, font=font)

        # 레벨별 회원수 화면에 쏘기
        level1 = 0
        level2 = 0
        level3 = 0
        level4 = 0
        for record in all_user_records:
            user_level = record[4]
            if int(user_level) // 100 >= 9:
                level4 += 1
            elif int(user_level) // 100 >= 8:
                level3 += 1
            elif int(user_level) // 100 >= 7:
                level2 += 1
            else:
                level1 += 1

        levels_arr = [level1,level2,level3,level4]
        for i in range(0, 4):
            self.canvas.create_text(900.0, 178.0 + i * 70.5, text=levels_arr[i], font=font)


        self.window.resizable(False, False)
        self.window.mainloop()

    def Back(self):
        from GUI.admin.AdminMenu.AdminMenu import AdminMenu
        self.window.withdraw()
        AdminMenu(self.window)

    # search버튼을 눌러서 나온 결과 => UserInfo2화면으로 넘어가는 함수
    def Next(self):
        global glo_user_info1
        um = UserDBManager()
        user_id = self.entry_1.get()
        user_id = process_str(user_id)
        glo_user_info1 = um.get_user_record(user_id)

        search_user_name = self.entry_1.get()
        if not is_str_valid(search_user_name):
            messagebox.showerror("사용자 검색 실패", "유효한 형식으로 입력하세요")
        else:
            self.window.withdraw()
            AdminUserInfo2(self.window, glo_user_info1) 
        
