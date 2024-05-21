import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from .AdminSearchVoca import word_exists

def delete_word(word_name):
    sheet = Sheet()
    wordsheets = sheet.wordsheets

    if(not word_exists(word_name)):
        return False
    sheet_num = __get_level_of_word(word_name)
    ws = wordsheets[sheet_num-1]
    row_idx = __get_row_loc_of_word(word_name)
    ws[f'A{row_idx}'] = ""
    ws[f'B{row_idx}'] = ""
    ws[f'C{row_idx}'] = ""
    sheet.save()
    return

def __get_row_loc_of_word(word_name):
    """
    get_row_loc_of_word는 단어의 열 번호를 정수값으로 반환합니다.
    """
    sheet = Sheet()
    wordsheets = sheet.wordsheets
    if not (word_exists(word_name)):
        return False
    for ws in wordsheets:
        idx_counter = 1
        for row in ws.iter_rows(min_row=2, max_col=1, max_row=ws.max_row, values_only=True):
            idx_counter += 1
            if word_name in row:
                return idx_counter
    return False

def __get_level_of_word(word_name):
    """
    get_row_loc_of_word는 단어의 레벨을 정수값으로 반환합니다.
    """
    sheet = Sheet()
    wordsheets = sheet.wordsheets
    if not word_exists(word_name):
        return False
    counter = 1
    for ws in wordsheets:
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
            if word_name in row:
                return counter
        counter += 1
    return False