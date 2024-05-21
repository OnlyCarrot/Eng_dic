import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

def get_all_word_records():
    """
    DB의 모든 단어의 array를 반환한다.
    """
    sheet = Sheet()
    wordsheets = sheet.wordsheets
    words = []
    for ws in wordsheets:
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
            if (not row[0] == None):
                words.append(row)
    return words