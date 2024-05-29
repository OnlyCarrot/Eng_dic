import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from func.admin.VocaManage.AdminSearchVoca import word_exists, get_row_loc_of_word, get_level_of_word, is_str_vaild, process_str
from func.admin.VocaManage.AdminViewVoca import AdminViewVoca

class DeleteVoca:
    def __init__(self):
        self.sheet = Sheet("wordsheet1")

    def delete_word(self, word_name):
        """
        DB에서 해당 단어를 삭제합니다.
        """
        wordsheets = self.sheet.wordsheets

        if(not is_str_vaild(word_name)): return False
        word_name = process_str(word_name)
        if not word_exists(word_name):
            return False
        
        adminViewVoca = AdminViewVoca()
        word_level = get_level_of_word(word_name)
        word_records = adminViewVoca.get_words_in_level(word_level)
        row_loc = get_row_loc_of_word(word_name)
        word_records = word_records[row_loc-1:]
        word_records.append((None, None, None))

        ws = wordsheets[word_level - 1]
        # 레코드를 한 칸씩 올리는 코드
        for record in word_records:
            ws[f'A{row_loc}'], ws[f'B{row_loc}'], ws[f'C{row_loc}'] = record
            row_loc += 1
        
        ws.delete_rows(ws.max_row, 1)
        #print("Max Row: ",ws.max_row)
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
        if not word_exists(ans):
            return False
        return True