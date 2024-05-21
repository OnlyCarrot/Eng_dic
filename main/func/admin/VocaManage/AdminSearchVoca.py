import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

#단어가 존재하는지를 확인하는 함수
def word_exists(word_name):
    sheet = Sheet()
    wordsheets = sheet.wordsheets
    for ws in wordsheets:
        # B열을 탐색하여 해당 word_name이 존재하는지 탐색한다.
        for row in ws.iter_rows(min_row=2, max_col=1, max_row=ws.max_row, values_only=True):
            if word_name in row:
                return True
    return False





