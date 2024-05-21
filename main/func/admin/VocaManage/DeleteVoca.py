import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from .AdminSearchVoca import word_exists, get_row_loc_of_word, get_level_of_word

def delete_word(word_name):
    """
    해당 단어를 DB에서 삭제합니다.
    """
    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets

    if(not word_exists(word_name)):
        return False
    sheet_num = get_level_of_word(word_name)
    ws = wordsheets[sheet_num-1]
    row_idx = get_row_loc_of_word(word_name)
    ws[f'A{row_idx}'] = ""
    ws[f'B{row_idx}'] = ""
    ws[f'C{row_idx}'] = ""
    sheet.save()
    return