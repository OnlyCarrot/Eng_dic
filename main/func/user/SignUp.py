from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet
from main.func.user import LevelTest


class SignUp:
    temp_id = ""
    temp_username = ""
    temp_password = ""
    def temp_storage(id, username, password):
        SignUp.temp_id = id
        SignUp.temp_username = username
        SignUp.temp_password = password

    def sign_up(level):
        loaded_xlsx = Sheet("usersheet")
        sheet = loaded_xlsx.worksheet
        workbook = loaded_xlsx.workbook

        # 마지막 행에 새로운 사용자 정보 추가
        new_user = [SignUp.temp_id, SignUp.temp_password, SignUp.temp_username, "user", level]
        sheet.append(new_user)

        # 엑셀 파일 저장
        workbook.save("main/DB/UserList.xlsx")

        print("추가되었습니다.")

    def is_str_vaild(entries):
        for entry in entries:
            if not entry.strip():
                return False
        return True

    def is_pw_dupli(pw1, pw2):
        if pw1 != pw2:
            return True
        else:
            return False
