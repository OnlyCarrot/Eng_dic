import tkinter as tk
from tkinter import messagebox
from administrator import adminVocaManagement
from administrator import userInformation


class AdminMenu(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("관리자 페이지")
        self.create_widgets()

    def create_widgets(self):
        # 메뉴 페이지 프레임
        menu_frame = tk.Frame(self.root)

        # 단어 관리 페이지
        btn_management_voca = tk.Button(
            menu_frame, text="단어 관리", command=self.voca_management_page
        )
        btn_management_voca.pack()

        # 사용자 조회 페이지
        btn_user_info = tk.Button(
            menu_frame, text="사용자 정보 조회", command=self.user_info_page
        )
        btn_user_info.pack()
        menu_frame.pack()

    def voca_management_page(self):
        # 메뉴 페이지 숨기기
        self.pack_forget()
        # 일일테스트 기능 페이지 표시
        adminVocaManagement.showPage(self.root, self)

    def user_info_page(self):
        # 메뉴 페이지 숨기기
        self.pack_forget()
        # 일일테스트 기능 페이지 표시
        userInformation.showPage(self.root, self)


def showPage(root):
    admin_menu = AdminMenu(root)
    admin_menu.pack()
