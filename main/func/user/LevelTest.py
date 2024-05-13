from openpyxl import load_workbook
import random


def select_random_word():
    # 엑셀 파일 열기
    workbook = load_workbook("main/DB/WordList.xlsx")

    # 시트 선택
    sheet = workbook["wordsheet"]

    word = []

    # num_words 만큼 반복하여 랜덤한 단어 추출
    for _ in range(40):
        # 랜덤한 행 번호 생성
        random_row_num = random.randint(1, sheet.max_row)

        # 랜덤한 행의 데이터 추출
        for row in sheet.iter_rows(random_row_num, random_row_num, values_only=True):
            word.append([row[0], row[1]])
    return word


def show_word_meaning(self, word):
    # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
    for i in range(0, 5):
        self.canvas.create_text(610.0, 130.0 + i * 53.5, text=word[i][1])
    # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
    for i in range(0, 5):
        self.canvas.create_text(950.0, 130.0 + i * 53.5, text=word[i + 5][1])


# user_input_word는 list로 받을거라 나중에 user_input_word[i] 로 수정
def grade_score(user_input_word, word):
    score = 0
    for i in range(0, len(word)):
        correct_answer = word[i][0]
        if user_input_word[0] == correct_answer:
            score += 1

    return score
