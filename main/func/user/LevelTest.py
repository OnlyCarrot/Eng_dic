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
                random_row_num = random.randint(2, sheet.max_row)

                # 랜덤한 행의 데이터 추출
                for row in sheet.iter_rows(random_row_num, random_row_num, values_only=True):
                    word.append([row[0], row[1]])

        return word
    
    def show_word_meaning1(self):
        word = LevelTest.select_word()
        # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 5][1])

    def show_word_meaning2(self):
        word = LevelTest.select_word()
        # 단어 뜻을 보여줌 x좌표가 610 에 11~15번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i + 10][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 16~20번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 15][1])
    
    def show_word_meaning3(self):
        word = LevelTest.select_word()
        # 단어 뜻을 보여줌 x좌표가 610 에 21~25번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i + 20][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 26~30번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 25][1])
    
    def show_word_meaning4(self):
        word = LevelTest.select_word()
        # 단어 뜻을 보여줌 x좌표가 610 에 31~35번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i + 30][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 36~40번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 35][1])

    # user_input_word는 list로 받을거라 나중에 user_input_word[i] 로 수정
    def grade_score(user_input_word, word):
        score = 0
        for i in range(0, len(word)):
            correct_answer = word[i][0]
            if user_input_word[0] == correct_answer:
                score += 1

        return score
    
    def is_str_vaild(ans):
        if(ans.strip() ==''):
            print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
            return False
        if(not ans.replace(' ', '').isalpha()):
            print("알파벳이 아닌 문자열이 입력되었습니다.")
            return False
        return True
    