from openpyxl import load_workbook
import random
import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class Daily:
    last_run_date =  None
    index = []

    #지금 날짜랑 비교해서 수행여부 확인
    def is_runned(user):
        Daily.last_run_date = user
        today = date.today()
        print(Daily.last_run_date, today)
        if Daily.last_run_date == today:
            print("오늘은 이미 daily_test를 실행했습니다.")
            return None
        
    def update_last_runned_date():
        #sheet 값 수정
        Daily.last_run_date = date.today()
        print(Daily.last_run_date, "로 업데이트 되었습니다")

    def daily_test(start_index, end_index):
        # start_col, end_col정보를 저장해서 넘김
        Daily.index.append(int(start_index) + 1)
        Daily.index.append(int(end_index) + 1)

    #area에 맞는 단어 뽑아오기
    def select_word():
        sheet = Sheet("wordsheet1").worksheet

        word = []
        for row in sheet.iter_rows(Daily.index[0], Daily.index[1], values_only=True):
            word.append([row[0], row[1]])

        # shuffle한 [단어, 뜻]값 return 
        random.shuffle(word) 
        return word 
    

    #뽑아온 단어 화면에 쏴주기
    def show_word_meaning(self):
        word = Daily.select_word()

        # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
        for i in range(0, 5):
            self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i][1])
        # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
        for i in range(0, 5):
            self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 5][1])

        return word

    def grade_score(user_input_word, word):
        score = 0
        for i in range(0, len(user_input_word)):
            correct_answer = word[i][0]
            if user_input_word[i] == correct_answer:
                score += 1

        return score
    
    def change_level(user_level, score):
        if(score == 10):
            user_level += 10
        elif(score >= 7):
            user_level += 5
        return user_level
    
    def is_digit_valid(ans):
        if ans.strip() == '':
            print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
            return False
        elif not ans.isdigit():
            print("숫자가 아닌 값이 입력되었습니다.")
            return False
        return True

    def is_str_valid(ans):
        if ans.strip() == '':
            print("공백 값이 입력되었습니다. 유효한 단어를 입력하세요.")
            return False
        if(not ans.replace(' ', '').isalpha()):
            print("알파벳이 아닌 문자열이 입력되었습니다.")
            return False
        return True

