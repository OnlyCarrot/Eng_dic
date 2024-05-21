import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from func.Sheet import Sheet

#단어가 존재하는지를 확인하는 함수
def word_exists(word_name):
    """
    DB에 해당 단어가 존재하면 True를, 존재하지 않으면 False를 반환합니다.
    """
    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets
    for ws in wordsheets:
        # B열을 탐색하여 해당 word_name이 존재하는지 탐색한다.
        for row in ws.iter_rows(min_row=2, max_col=1, max_row=ws.max_row, values_only=True):
            if word_name in row:
                return True
    return False

def get_word_record(word_name):
    """
        해당 단어의 레코드를 반환합니다.
    """
    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets
    if not word_exists(word_name):
        return False

    for ws in wordsheets:
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
            if word_name in row:
                return row
    return False


def get_row_loc_of_word(word_name):
    """
    단어의 열 번호(엑셀의 열 번호)를 정수값으로 반환합니다.
    """
    sheet = Sheet("wordsheet1")
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

def get_level_of_word(word_name):
    """
    단어의 레벨을 정수값으로 반환합니다.
    1,2,3,4 중 하나의 값이 반환됩니다.
    """
    sheet = Sheet("wordsheet1")
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



print(get_word_record("apply for"))