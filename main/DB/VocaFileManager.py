import os
from openpyxl import load_workbook

cwd = os.getcwd()

# 단어 엑셀 파일이 있는 경로이다.
voca_file_path = f"{cwd}\\main\\DB\\WordList.xlsx"

# 엑셀 파일을 불러온다.
wb = load_workbook(voca_file_path)

def get_word(word_name):
    if(word_name):
        pass
    else:
        return False
    
def delete_word(word_name):
    if(word_name):
        # 해당 영어 단어가 있는 행을 지워라.
        pass
    else:
        return False
    
def edit_word(word_name):
    if(word_name):
        # 해당 영어 단어가 있는 행에서 뜻과 품사 부분을 수정하게 해라.
        pass
    else:
        return False

