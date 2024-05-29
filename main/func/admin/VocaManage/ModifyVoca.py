import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

from func.admin.VocaManage.AdminSearchVoca import get_row_loc_of_word, get_level_of_word

class ModifyVoca:
    def __init__(self):
        self.sheet = Sheet("wordsheet1")

    def edit_word(self, word_name, modify_eng, kor_meaning, word_class):
        wordsheets = self.sheet.wordsheets
    
        sheet_num = get_level_of_word(word_name)
        row_idx = get_row_loc_of_word(word_name)
        ws = wordsheets[sheet_num - 1]
        ws[f'A{row_idx}'] = modify_eng
        ws[f'B{row_idx}'] = kor_meaning
        ws[f'C{row_idx}'] = word_class
        self.sheet.save()
        return

    def is_str_valid(self, ans):
        if ans.strip() == '':
            print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
            return False
        # 공백을 제거한 문자열이 모두 알파벳인지 확인
        if not ans.replace(' ', '').isalpha():
            print("알파벳과 공백이 아닌 문자열이 입력되었습니다.")
            return False
        return True
