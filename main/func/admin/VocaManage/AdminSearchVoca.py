import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from func.Sheet import Sheet


def is_str_vaild(word_name):
    """
    사용자나 유저가 입력한 문자열의 유효성을 판단합니다.
    입력받은 문자의 좌 우 공백을 제거하고, 영문자를 소문자로 바꾼 후 반환합니다.
    영문자가 아닌 기호가 들어간 경우에는 False를 반환합니다.
    """
    if(word_name.strip() ==''):
        print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
        return False
    
    if(not word_name.replace(' ', '').isalpha()):
        print("알파벳이 아닌 문자열이 입력되었습니다.")
        return False
    return True

def process_str(word_name):
    word_name = word_name.lstrip().rstrip()
    word_name = word_name.lower()
    word_name = word_name.replace("  ", '')
    return word_name

def word_exists(word_name):
    """
    DB에 해당 단어가 존재하면 True를, 존재하지 않으면 False를 반환합니다.
    """
    if(not is_str_vaild(word_name)): return False
    word_name = process_str(word_name)
    if(word_name == ''): return False
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

    
    if(not is_str_vaild(word_name)): return False
    word_name = process_str(word_name)
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

    if(not is_str_vaild(word_name)): return False
    word_name = process_str(word_name)
    if not word_exists(word_name):
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

    if(not is_str_vaild(word_name)): return False
    word_name = process_str(word_name)
    if not word_exists(word_name):
        return False
    
    counter = 1
    for ws in wordsheets:
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
            if word_name in row:
                return counter
        counter += 1
    return False
