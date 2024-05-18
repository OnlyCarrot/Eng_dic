from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from main.func.Sheet import Sheet

class Voca:
    def __init__(self):
        sheets = [
            Sheet("wordsheet1").worksheet,
            Sheet("wordsheet2").worksheet,
            Sheet("wordsheet3").worksheet,
            Sheet("wordsheet4").worksheet
        ]
        # 모든 시트 객체를 리스트로 저장
        self.sheets = sheets
            
    def show_voca(self):    
        for sheet in self.sheets:
            for row in sheet.iter_rows(values_only=True):
                eng, kor, c = row
                print(eng, kor, c)
            
    def search_voca(self, input):
        for sheet in self.sheets:
            for row in sheet.iter_rows(values_only=True):
                eng, kor, c = row
                if input == eng:
                    print(eng, kor, c)
                    return True
        return False

Voca().show_voca()
print(Voca().search_voca("apply for"))