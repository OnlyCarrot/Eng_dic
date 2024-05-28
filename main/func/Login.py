from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet
from func.User import User

class Login:
    def __init__(self):
        self.sheet = Sheet("usersheet").worksheet
        self.user = User()


    def login(self, id, password):
        # 시트를 순회하며 사용자의 로그인 정보와 맞는 행의 모든 정보를 return
        for row in self.sheet.iter_rows(values_only=True):
            name = row[2]
            role = row[3]
            level = row[4]
            last_test_date = row[5]
            if id == row[0] and password == row[1]:
                self.user.save_user(id, password, name, role, level, last_test_date)
                return True
        return False