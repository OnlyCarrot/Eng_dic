import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from func.Login import login

#로그인 검증
print(login("user1", "pw1"))
print(login("user", "pw1"))