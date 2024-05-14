def daily_test(start_column, end_column):
    # start_col, end_col정보를 저장해서 넘김
    col_num = [start_column, end_column]

    return col_num


def show_word_meaning(self, col_num):
    sheet = open_sheet.wordsheet("wordsheet1")

    word = []

    for row in sheet.iter_rows(col_num[0], col_num[1], values_only=True):
        word.append([row[0], row[1]])

    # shuffle한 값으로 저장
    random.shuffle(word)

    # 단어 뜻을 보여줌 x좌표가 610 에 1~5번 단어
    for i in range(0, 5):
        self.canvas.create_text(460.0, 130.0 + i * 53.5, text=word[i][1])
    # 단어 뜻을 보여줌 x좌표가 950 에 6~10번 단어
    for i in range(0, 5):
        self.canvas.create_text(800.0, 130.0 + i * 53.5, text=word[i + 5][1])

    # 단어 [영어,뜻] 담은 list return
    return word


# user_input_word는 list로 받을거라 나중에 user_input_word[i] 로 수정
def grade_score(user_input_word, word):
    score = 0
    for i in range(0, len(word)):
        correct_answer = word[i][0]
        if user_input_word[0] == correct_answer:
            score += 1

    return score