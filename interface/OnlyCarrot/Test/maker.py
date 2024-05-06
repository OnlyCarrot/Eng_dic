import pandas as pd
import random

def maker(n, s):
    xl = pd.ExcelFile('WordList.xlsx')
    sheets = xl.sheet_names
    eng_list = []
    kor_list = []
    
    # 각 시트에 대해 작업 수행
    for sheet in sheets:
        # 시트별 데이터 불러오기
        df = xl.parse(sheet)
        # 각 단계에 따라 영어 단어 수 계산
        if s == 0:
            eng_count = [n // 4] * 4
        elif s == 1:
            eng_count = [n * (4-i) // 10 for i in range(4)]
        elif s == 2:
            eng_count = [n * (3-i) // 10 for i in range(4)]
        elif s == 3:
            eng_count = [n * (3-i) // 10 for i in range(4)]
            eng_count[1], eng_count[2] = eng_count[2], eng_count[1]
        elif s == 4:
            eng_count = [n * (3-i) // 10 for i in range(4)]
            eng_count[0], eng_count[1] = eng_count[1], eng_count[0]
        
        # 영어 단어와 한글 뜻 추출
        for i, count in enumerate(eng_count):
            words = random.sample(range(2, df.shape[0]), count)
            for word in words:
                eng_word = df.iloc[word, 0]
                kor_word = df.iloc[word, 1]
                eng_list.append(eng_word)
                kor_list.append(kor_word)
    
    return eng_list, kor_list
