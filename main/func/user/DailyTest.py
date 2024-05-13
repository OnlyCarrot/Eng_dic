from openpyxl import load_workbook


def daily_test(start_column, end_column):
    # start_col, end_col정보를 저장해서 넘김
    col_num = [start_column, end_column]

    return col_num


def show_word_meaning(self, col_num):
    # 엑셀 파일 열기
    workbook = load_workbook("main/DB/WordList.xlsx")

    # 시트 선택
    sheet = workbook["wordsheet"]

    i = 0
    j = 0

    # 단어 뜻을 보여줌 start_column ~ start_column + 5 까지는 x좌표가 610
    for row in sheet.iter_rows(col_num[0], col_num[1] - 5, values_only=True):
        self.canvas.create_text(610.0, 130.0 + i * 53.5, text=row[0])
        i += 1
    # start_column + 5 ~ end_column 까지는 x좌표가 950
    for row in sheet.iter_rows(col_num[0] + 5, col_num[1], values_only=True):
        self.canvas.create_text(950.0, 130.0 + j * 53.5, text=row[0])
        j += 1
