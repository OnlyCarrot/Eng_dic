import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from func.User import User
from func.UserDBManager import UserDBManager

user = User()
user.save_user(1, "password", "name", "role", "level", "2024-05-05")

id = user.get_id()
password = user.get_password()
name = user.get_name()
role = user.get_role()
level = user.get_level()
last_test_date = user.get_last_test_date()

#제대로 저장되었는지 확인
print("{}, {}, {}, {}, {}, {}".format(id, password, name, role, level, last_test_date))
#user1의 row위치 불러오기 
userDBManager = UserDBManager()
print("user id = {}".format(userDBManager.get_idx_of_user("user1")))