import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from func.Sheet import Sheet

sheet = Sheet("usersheet").worksheet
#Sheet가 제대로 불러져 왔는지 확인
print(sheet.title)