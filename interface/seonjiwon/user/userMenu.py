import tkinter as tk
from tkinter import messagebox
from user import userDailyVocaTest
from user import userVocaSearch


class UserMenu(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("사용자 페이지")
        self.create_widgets()

    def create_widgets(self):
        # 기능 페이지 프레임
        menu_frame = tk.Frame(self.root)

        # 일일 테스트 페이지
        btn_daily_test = tk.Button(
            menu_frame, text="일일 테스트", command=self.daily_test_page
        )
        btn_daily_test.pack()

        # 단어장 조회 페이지
        btn_search_vocabulary = tk.Button(
            menu_frame, text="단어장 조회", command=self.voca_search_page
        )
        btn_search_vocabulary.pack()

        menu_frame.pack()

    def daily_test_page(self):
        # 메뉴 페이지 숨기기
        self.pack_forget()
        # 일일테스트 기능 페이지 표시
        userDailyVocaTest.showPage(self.root, self)

    def voca_search_page(self):
        # 메뉴 페이지 숨기기
        self.pack_forget()
        # 일일테스트 기능 페이지 표시
        userVocaSearch.showPage(self.root, self)


def showPage(root):
    user_menu = UserMenu(root)
    user_menu.pack()
