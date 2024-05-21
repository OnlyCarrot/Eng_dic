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


# private 함수이다.
# delete_word()안에서 사용될 서브함수이므로, 그 밖에서는 사용할 필요는 없습니다.
def __pull_up(word_name):
    """
        단어가 삭제되면 삭제된 단어 아래부터 한 칸 씩 올린다.
    """

    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets
    word_level = get_level_of_word(word_name)
    row_loc = get_row_loc_of_word(word_name)
    ws = wordsheets[word_level - 1]
    max_row = ws.max_row

    # 여기서부터는 for문으로 밀어 올리는 코드를 구현해야 함

    return
