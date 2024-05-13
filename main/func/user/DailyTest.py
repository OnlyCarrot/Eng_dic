from openpyxl import load_workbook


def daily_test(start_column, end_column):
    # 엑셀 파일 열기
    workbook = load_workbook("main/DB/WordList.xlsx")

    # 시트 선택
    sheet = workbook["wordsheet"]

    # 데이터 저장할 리스트 초기화
    data = []

    # 시트를 순회하며 사용자의 로그인 정보와 맞는 행의 모든 정보를 return
    for row in sheet.iter_rows(start_column, end_column, values_only=True):
        print(row[0], row[1], row[2], end="\n")
