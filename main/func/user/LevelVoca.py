from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet
from main.func.Word import Word

class LevelVoca:
    def __init__(self):
        self.sheet = Sheet("wordsheet1").worksheet

    def show_word(self, level):    
        for row in self.sheet.iter_rows(values_only=True):
            eng, kor, c = row
            print(eng, kor, c)
            
    def search_voca(self, input):
        for row in self.sheet.iter_rows(values_only=True):
            eng, kor, c = row
            if(input == eng):
                print(eng, kor, c)
                return True
        return False
        

#LevelVoca().show_word(1)
print(LevelVoca().search_voca("apply for"))