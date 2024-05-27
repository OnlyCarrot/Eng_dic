import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.user.DailyTest import Daily

Daily.daily_test(1, 10)
#점수에 맞는 갑을 가져오는지 테스트
print(Daily.select_word(700))