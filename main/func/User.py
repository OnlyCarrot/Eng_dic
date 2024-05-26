import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class User(metaclass=Singleton):
    def __init__(self):
        self.user_data = {}
        self.sheet = Sheet("usersheet")
        self.ws = self.sheet.worksheet
        self.wb = self.sheet.workbook
    
    def save_user(self, id, password, name, role, level, last_test_date):
        self.user_data = {
            'id': id,
            'password': password,
            'name': name,
            'role': role,
            'level': level,
            'last_test_date': last_test_date
        }
    
    def get_id(self):
        return self.user_data.get('id')
    
    def get_password(self):
        return self.user_data.get('password')
    
    def get_name(self):
        return self.user_data.get('name')
    
    def get_role(self):
        return self.user_data.get('role')
    
    def get_level(self):
        return self.user_data.get('level')
    
    def get_last_test_date(self):
        return self.user_data.get('last_test_date')
    
    # 해당 유저가 있는 행의 번호를 반환한다.
    def get_idx_of_user(self, user_id):
        #if self.user_exists(user_id):
        idx_counter = 1
        for row in self.ws.iter_rows(min_row=2, max_col=1, max_row=self.ws.max_row, values_only=True):
            idx_counter += 1
            if user_id in row:
                break
        return idx_counter
    
    def edit_user(self, user_id_index,id, password, name, role, update_level, today):
        print(user_id_index)
        self.ws[f'A{user_id_index}'] = id
        self.ws[f'B{user_id_index}'] = password
        self.ws[f'C{user_id_index}'] = name
        self.ws[f'D{user_id_index}'] = role
        self.ws[f'E{user_id_index}'] = update_level
        self.ws[f'F{user_id_index}'] = today

        self.wb.save("main/DB/UserList.xlsx")