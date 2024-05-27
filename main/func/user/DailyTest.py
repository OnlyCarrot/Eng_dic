from openpyxl import load_workbook
import random
from tkinter import messagebox
import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class Daily:
    index = []
        
    def update_user(score, user):
        #sheet 값 수정            
        user_id_index = user.get_idx_of_user(user.get_id())
        if(score == 10):
            user.edit_user(user_id_index, user.get_id(), user.get_password(), user.get_name(), user.get_role(), user.get_level() + 10, date.today())
        elif(score > 5):
            user.edit_user(user_id_index, user.get_id(), user.get_password(), user.get_name(), user.get_role(), user.get_level() + 5, date.today())
        else:
            user.edit_user(user_id_index, user.get_id(), user.get_password(), user.get_name(), user.get_role(), user.get_level(), date.today())
        print(date.today(), "로 업데이트 되었습니다")

    def daily_test(start_index, end_index):
        # start_col, end_col정보를 저장해서 넘김
        Daily.index.append(int(start_index) + 1)
        Daily.index.append(int(end_index) + 1)

    #area에 맞는 단어 뽑아오기
    def select_word(level):
        if(level < 600):
            sheet = Sheet("wordsheet1").worksheet
        elif(level < 700):
            sheet = Sheet("wordsheet2").worksheet
        elif(level < 800):
            sheet = Sheet("wordsheet3").worksheet
        elif(level < 900):
            sheet = Sheet("wordsheet4").worksheet  

        word = []
        for row in sheet.iter_rows(Daily.index[0], Daily.index[1], values_only=True):
            word.append([row[0], row[1]])

        # shuffle한 [단어, 뜻]값 return 
        random.shuffle(word) 
        return word 
    

    #뽑아온 단어 화면에 쏴주기
    def show_word_meaning(self, level):
        word = Daily.select_word(level)

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

