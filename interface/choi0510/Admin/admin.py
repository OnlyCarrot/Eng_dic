from tkinter import *
from center_window import center_window
from Admin.VocaManagement import AddWordPage, DeleteWordPage, EditWordPage
from Admin.UserInfo import ViewLevelPage, ViewDistributionPage

class AdminPage:
    def __init__(self, parent):
        self.parent = parent
        self.window = Toplevel(self.parent)
        self.window.title("관리자 페이지")
        self.window.geometry("1200x500")
        center_window(self.window, 1200, 500)

        label = Label(self.window, text="관리자 페이지")
        label.pack(pady=10)

        # Add Word Button
        add_word_button = Button(self.window, text="단어 추가", command=self.open_add_word_page)
        add_word_button.pack(pady=5)

        # Delete Word Button
        delete_word_button = Button(self.window, text="단어 삭제", command=self.open_delete_word_page)
        delete_word_button.pack(pady=5)

        # Edit Word Button
        edit_word_button = Button(self.window, text="단어 수정", command=self.open_edit_word_page)
        edit_word_button.pack(pady=5)

        # View Level by User Button
        view_level_button = Button(self.window, text="사용자별 레벨 조회", command=self.open_view_level_page)
        view_level_button.pack(pady=5)

        # View Level Distribution by User Button
        view_distribution_button = Button(self.window, text="사용자 전체 레벨 분포", command=self.open_view_distribution_page)
        view_distribution_button.pack(pady=5)

        # Back to Login Button
        back_to_login_button = Button(self.window, text="로그인 화면으로 돌아가기", command=self.back_to_login)
        back_to_login_button.pack(pady=5)

    def open_add_word_page(self):
        self.window.withdraw()  # Hide the admin page window
        AddWordPage(self.window)  # Open the AddWordPage

    def open_delete_word_page(self):
        self.window.withdraw()  # Hide the admin page window
        DeleteWordPage(self.window)  # Open the DeleteWordPage

    def open_edit_word_page(self):
        self.window.withdraw()  # Hide the admin page window
        EditWordPage(self.window)  # Open the EditWordPage

    def open_view_level_page(self):
        self.window.withdraw()  # Hide the admin page window
        ViewLevelPage(self.window)  # Open the ViewLevelPage

    def open_view_distribution_page(self):
        self.window.withdraw()  # Hide the admin page window
        ViewDistributionPage(self.window)  # Open the ViewDistributionPage

    def back_to_login(self):
        # Destroy the admin page window
        self.window.destroy()
        # Show the login window
        self.parent.deiconify()
