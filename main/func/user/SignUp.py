from openpyxl import load_workbook
from func.globalFunc import open_sheet



def sign_up(id, username, password, role, level):
    sheet = open_sheet.usersheet()

    # 마지막 행에 새로운 사용자 정보 추가
    new_user_data = [id, username, password, role, level]
    sheet.append(new_user_data)

    # 엑셀 파일 저장
    #sheet.save("main/DB/UserList.xlsx")

    print("추가되었습니다.")