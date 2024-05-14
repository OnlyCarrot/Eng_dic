main/func/Login.py
from openpyxl import load_workbook
from func.globalFunc import open_sheet



def login_validation(entered_id, entered_password):
    sheet = open_sheet.usersheet()

    # 데이터 저장할 리스트 초기화
    data = []

    # 시트를 순회하며 사용자의 로그인 정보와 맞는 행의 모든 정보를 return
    for row in sheet.iter_rows(values_only=True):
        name = row[2]
        role = row[3]
        level = row[4]
        if entered_id == row[0] and entered_password == row[1]:
            data.extend([entered_id, entered_password, name, role, level])
            return data

    return False