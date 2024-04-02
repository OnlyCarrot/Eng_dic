import openpyxl as op

wb = op.load_workbook("C:\\Eng_dic\\Trash\\test_excel_py\\pytest.xlsx")

def pickup(sheet_name, row_num, col_num):
    ws = wb[sheet_name]
    data1 = ws.cell(row = row_num, column = col_num).value
    print(data1)

pickup("과일",3,2)
pickup("사물",4,2)