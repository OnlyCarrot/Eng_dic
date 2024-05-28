import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.user.SignUp import SignUp

#Test: 새로운 user가 UserList에 추가 되는지 확인
SignUp.temp_storage("test", "test", "test")
SignUp.sign_up(666)
