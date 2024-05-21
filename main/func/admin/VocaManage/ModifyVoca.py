import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from AdminSearchVoca import word_exists, get_row_loc_of_word, get_level_of_word

def edit_word(word_name, kor_meaning, word_class):
    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets
    if(not word_exists(word_name)):
        return False
    
    sheet_num = get_level_of_word(word_name)
    row_idx = get_row_loc_of_word(word_name)
    ws = wordsheets[sheet_num - 1]
    ws[f'B{row_idx}'] = kor_meaning
    ws[f'C{row_idx}'] = word_class
    sheet.save()
    return
