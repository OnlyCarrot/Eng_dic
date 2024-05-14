from openpyxl import load_workbook
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
from func.Sheet import Sheet

class UserInfo:
    def __init__(self):
        self.sheet = Sheet("usersheet").worksheet
        
    
    def show_selected_user(self, user_id):
        for row in self.sheet.iter_rows(values_only=True):
            id, password, name, role, level = row
            if(user_id == id):
                print(id, password, name, role, level)

    def show_all_user(self):
        for row in self.sheet.iter_rows(values_only=True):
            id, password, name, role, level = row
            if(not id.startswith("ad")):
                print(id, password, name, role, level)

UserInfo().show_selected_user("user1")
UserInfo().show_all_user()
            