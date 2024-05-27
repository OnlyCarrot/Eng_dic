import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from func.user.SignUp import sign_up, temp_storage

#Test: 새로운 user가 UserList에 추가 되는지 확인
temp_storage("test", "test", "test")
sign_up(666)
