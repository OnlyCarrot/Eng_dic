from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet
from main.func.user import LevelTest



def sign_up(id, username, password, role, level):
    # 레벨 테스트를 통해 얻은 점수를 가져옴
    score = LevelTest.grade_score()

    loaded_xlsx = Sheet("usersheet")
    sheet = loaded_xlsx.worksheet
    workbook = loaded_xlsx.workbook

    # 마지막 행에 새로운 사용자 정보 추가
    new_user = [id, username, password, role, level]
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