import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

def edit_word(self, word_name, kor_meaning, word_class):
    if(not self.word_exists(word_name)):
        return False
    
    sheet_num = self.get_level_of_word(word_name)
    row_idx = self.get_row_loc_of_word(word_name)
    ws = self.wordsheets[sheet_num - 1]
    ws[f'B{row_idx}'] = kor_meaning
    ws[f'C{row_idx}'] = word_class
    self.wb.save(voca_file_path)
    return