from openpyxl import load_workbook


def sign_up(id, username, password, role, level):
    # 엑셀 파일 열기
    workbook = load_workbook("main/DB/UserList.xlsx")

    # 시트 선택
    sheet = workbook["usersheet"]

    # 마지막 행에 새로운 사용자 정보 추가
    new_user_data = [id, username, password, role, level]
    sheet.append(new_user_data)

    # 엑셀 파일 저장
    workbook.save("main/DB/UserList.xlsx")

    print("추가되었습니다.")