import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from AdminSearchVoca import word_exists, get_row_loc_of_word, get_level_of_word, get_word_record
from AdminViewVoca import get_words_in_level

def delete_word(word_name):
    """
        DB에서 해당 단어를 삭제합니다.
    """
    sheet = Sheet("wordsheet1")
    wordsheets = sheet.wordsheets

    if(not word_exists(word_name)):
        return False
    
    word_level = get_level_of_word(word_name)
    word_records = get_words_in_level(word_level)
    row_loc = get_row_loc_of_word(word_name)
    word_records = word_records[row_loc-1:]
    word_records.append(("","",""))

    print(word_records)

    ws = wordsheets[word_level - 1]
    max_row = ws.max_row

    # 레코드를 한 칸씩 올리는 코드
    for record in word_records:
        ws[f'A{row_loc}'], ws[f'B{row_loc}'], ws[f'C{row_loc}'] = record
        row_loc += 1
        #print(row_loc)
        #sheet.save()
    sheet.save()
    #print("max_row:", max_row)
    return
