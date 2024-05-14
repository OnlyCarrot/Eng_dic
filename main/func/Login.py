from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from func.User import User



def login_validation(id, password):
    sheet = Sheet("usersheet").worksheet


    # 시트를 순회하며 사용자의 로그인 정보와 맞는 행의 모든 정보를 return
    for row in sheet.iter_rows(values_only=True):
        name = row[2]
        role = row[3]
        level = row[4]
        if id == row[0] and password == row[1]:
            user = User(id, password, name, role, level)
            return user

    return False