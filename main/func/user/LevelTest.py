from openpyxl import load_workbook
import random
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class LevelTest:

    def select_word():
        word = []

        # 각 시트에서 10개씩 단어 추출
        for sheet_num in range(1, 5):
            sheet_name = f"wordsheet{sheet_num}"
            sheet = Sheet(sheet_name).worksheet

            # 각 시트에서 10번씩 랜덤한 단어 추출
            for _ in range(10):
                # 랜덤한 행 번호 생성
                random_row_num = random.randint(1, sheet.max_row)

                # 랜덤한 행의 데이터 추출
                for row in sheet.iter_rows(random_row_num, random_row_num, values_only=True):
                    word.append([row[0], row[1]])

        return word
    """
    def select_word():
        sheet = Sheet("wordsheet1").worksheet
        word = []

        # num_words 만큼 반복하여 랜덤한 단어 추출
        for _ in range(40):
            # 랜덤한 행 번호 생성
            random_row_num = random.randint(1, sheet.max_row)

            # 랜덤한 행의 데이터 추출
            for row in sheet.iter_rows(random_row_num, random_row_num, values_only=True):
                word.append([row[0], row[1]])
        return word
    """

    def show_word_meaning(self, word):
        # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 5][1])


    # user_input_word는 list로 받을거라 나중에 user_input_word[i] 로 수정
    def grade_score(user_input_word, word):
        score = 0
        for i in range(0, len(word)):
            correct_answer = word[i][0]
            if user_input_word[0] == correct_answer:
                score += 1

        return score