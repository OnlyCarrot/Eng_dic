import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.admin.VocaManage.AdminViewVoca import get_all_word_records, get_words_in_level

#Test
#print(get_all_word_records())
print(get_words_in_level(1))