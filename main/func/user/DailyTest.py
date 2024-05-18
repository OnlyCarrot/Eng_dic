from openpyxl import load_workbook
import random
import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class Daily:
    #마지막 테스트 수행일을 담음
    last_run_date = None

    #지금 날짜랑 비교해서 수행여부 확인
    def is_runned():
        today = date.today()
        print(Daily.last_run_date)
        print(today)
        if Daily.last_run_date == today:
            print("오늘은 이미 daily_test를 실행했습니다.")
            return None
        
        Daily.last_run_date = today
        print(Daily.last_run_date)

    def daily_test(start_index, end_index):
        # start_col, end_col정보를 저장해서 넘김
        return [start_index, end_index]

    #area에 맞는 단어 뽑아오기
    def select_word(index):
        sheet = Sheet("wordsheet1").worksheet

        word = []
        for row in sheet.iter_rows(index[0], index[1], values_only=True):
            word.append([row[0], row[1]])

        # shuffle한 [단어, 뜻]값 return 
        random.shuffle(word) 
        return word 

    #뽑아온 단어 화면에 쏴주기
    def show_word_meaning(self, index):
        word = Daily.select_word(index)

        # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 5][1])

        return word


    # user_input_word는 list로 받을거라 나중에 user_input_word[i] 로 수정
    def grade_score(user_input_word, word):
        score = 0
        for i in range(0, len(word)):
            correct_answer = word[i][0]
            if user_input_word[0] == correct_answer:
                score += 1

        return score
    
    def change_level(user_level, score):
        if(score == 10):
            user_level += 10
        elif(score >= 7):
            user_level += 5 
        return user_level

    
#Test
#Daily.is_runned()
print(Daily.change_level(600, 10))
