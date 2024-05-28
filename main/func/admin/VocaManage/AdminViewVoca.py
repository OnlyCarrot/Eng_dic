import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

# def get_all_word_records():
#     """
#     DB속 모든 단어 레코드를 반환합니다.
#     첫 번째 레벨부터 네 번째 레벨까지 모두 반환합니다.
#     """
#     sheet = Sheet("wordsheet1")
#     wordsheets = sheet.wordsheets
#     words = []
#     for ws in wordsheets:
#         for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
#             if (not row[0] == None):
#                 words.append(row)
#     return words

class AdminViewVoca():
    def __init__(self):
        self.sheet = Sheet("wordsheet1")
    def get_words_in_level(self, word_level):
        """
        DB속 해당 레벨에 맞는 단어 레코드를 반환합니다.
        첫 번째 매개변수에는 1,2,3,4 중 하나를 입력합니다.
        """
        wordsheets = self.sheet.wordsheets
        if (not word_level in (1,2,3,4)):
            print("word_level 값이 잘못되었습니다.")
            return False
        ws = wordsheets[word_level - 1]
        words = []
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
            if (not row[0] == None):
                words.append(row)
        return words