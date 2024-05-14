from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet



def sign_up(id, username, password, role, level):
    loaded_xlsx = Sheet("usersheet")
    sheet = loaded_xlsx.worksheet
    workbook = loaded_xlsx.workbook

    # 마지막 행에 새로운 사용자 정보 추가
    new_user = [id, username, password, role, level]
    sheet.append(new_user)

    # 엑셀 파일 저장
    workbook.save("main/DB/UserList.xlsx")

    print("추가되었습니다.")