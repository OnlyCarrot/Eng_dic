import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from func.admin.VocaManage.AdminSearchVoca import word_exists, get_row_loc_of_word, get_level_of_word, get_word_record,is_str_vaild, process_str

class AddWord:
    def add_word(word_name, kor_meaning, word_class, word_level):
        """
            DB에 새로운 단어를 추가합니다.
            word_name: 영어 단어명
            kor_meaning: 한국어 해석
            word_class: 품사
            word_level: 단어의 레벨(1,2,3,4 중 하나)

        """
        sheet = Sheet("wordsheet1")
        wordsheets = sheet.wordsheets

        if(kor_meaning.strip() == ''):
            print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
            return False
        
        # Check if word_class is valid
        valid_word_classes = {"n", "v", "adj", "adv", "phr", "prep"}
        if word_class not in valid_word_classes:
            print("word_class는 n, v, adj, adv, phr, prep 중 하나여야 합니다.")
            return False

        # Check if the word is already in the Excel file
        if word_exists(word_name):
            print(f"The word '{word_name}' already exists in DB.")
            print("Go to Edit Word page.")
            return False

        if (not word_level in (1,2,3,4)):
            print("word_level 값이 잘못되었습니다.")
            return False
        
        ws = wordsheets[word_level - 1]

        # Find the first empty row in the worksheet
        empty_row = ws.max_row + 1
        
        # Write the data to the next empty row
        ws[f'A{empty_row}'] = word_name
        ws[f'B{empty_row}'] = kor_meaning
        ws[f'C{empty_row}'] = word_class
        
        sheet.save()
        return True

