from pathlib import Path
from tkinter import *
from tkinter import messagebox
from User.mainpage import MainWindow
from Admin.admin import AdminPage
from signup import SignupPage
from center_window import center_window  # center_window 모듈 가져오기

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_main_page():
    MainWindow(window)

def open_admin_page():
    window.withdraw()
    AdminPage(window)

def signup():
    window.withdraw()
    SignupPage(window)

def check_credentials():
    # 입력된 사용자 이름과 비밀번호 가져오기
    entered_username = entry_1.get()
    entered_password = entry_2.get()
    
    # 입력된 값과 저장된 값 비교
    if entered_username == "admin" and entered_password == "adminpassword":
        messagebox.showinfo("로그인 성공", "관리자님, 환영합니다!")
        open_admin_page()
    elif entered_username == saved_username and entered_password == saved_password:
        # 일치할 경우 메인 화면으로 이동하는 기능 추가
        messagebox.showinfo("로그인 성공", "환영합니다!")
        open_main_page()
        # 메인 화면으로 이동하는 코드 작성
    else:
        # 불일치할 경우 메시지 출력
        messagebox.showerror("로그인 실패", "사용자 이름 또는 비밀번호가 올바르지 않습니다.")


window = Tk()

window.title("수준별 토익 영단어 프로그램")
window.geometry("1200x500")
window.configure(bg = "#FFFFFF")

center_window(window, 1200, 500)

saved_username = "user"
saved_password = "password"

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    600.0,
    250.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    237.0,
    221.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    254.0,
    431.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    900.0,
    250.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    905.0,
    80.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    913.0,
    150.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    906.0,
    229.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    906.0,
    342.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    802.0,
    211.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    802.0,
    322.0,
    image=image_image_10
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    908.0,
    241.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=728.0,
    y=224.0,
    width=360.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    908.5,
    351.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=728.5,
    y=334.0,
    width=360.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_credentials,
    relief="flat"
)
button_1.place(
    x=704.0,
    y=402.0,
    width=196.0,
    height=77.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=signup,
    relief="flat"
)
button_2.place(
    x=924.0,
    y=402.0,
    width=196.0,
    height=77.0
)

window.resizable(True, True)
window.mainloop()
