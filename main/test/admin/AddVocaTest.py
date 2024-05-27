import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.admin.VocaManage.AddVoca import add_word

#Test: 단어가 제대로 추가되는지 테스트
#add_word("testtest", "테스트", "n", 1)

#Test: 유효성 검사 테스트
add_word("testtest", "", "n", 1)
add_word("testtest", "테스트", "", 1)
add_word("testtest", "테스트", "n", 8)