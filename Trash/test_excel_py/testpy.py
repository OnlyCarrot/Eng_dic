import pandas as pd

file_path = "C:\\Eng_dic\\Trash\\test_excel_py\\pytest.xlsx"

data1 = pd.read_excel(file_path, sheet_name='과일', index_col='id')
data2 = pd.read_excel(file_path, sheet_name='사물', index_col='id')
print(data1)
print("===========================")
print(data2)