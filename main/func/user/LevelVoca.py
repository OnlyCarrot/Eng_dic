from openpyxl import load_workbook
from tkinter import END
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class LevelVoca:
    def __init__(self):
        self.sheet1 = Sheet("wordsheet1").worksheet
        self.sheet2 = Sheet("wordsheet2").worksheet
        self.sheet3 = Sheet("wordsheet3").worksheet
        self.sheet4 = Sheet("wordsheet4").worksheet

    def show_word(self, listbox, level):
        if(level < 600):
            sheet = self.sheet1
        elif(level < 700):
            sheet = self.sheet2    
        elif(level < 800):
            sheet = self.sheet3    
        elif(level < 900):
            sheet = self.sheet4    

        # 리스트박스 초기화
        listbox.delete(0, END)
        
        # 단어장 데이터를 리스트박스에 추가
        i = 1
        for row in sheet.iter_rows(2, values_only=True):
            eng, kor, c = row
            listbox.insert(END, f"{i}    {eng} - {kor} - {c}")
            i+=1

