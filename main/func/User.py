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
    
    