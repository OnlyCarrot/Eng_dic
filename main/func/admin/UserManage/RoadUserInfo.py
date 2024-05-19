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

    def show_total_user_count(self):
        total_user_count = 0 
        for row in self.sheet.iter_rows(values_only=True):
            for role in row:
                if role == "user":
                    total_user_count += 1
        print("총 사용자 수:", total_user_count)
        


    # 숫자 표기를 통한 분포도 확인
    def show_distribution_user(self):
        levels_count = {1: 0, 2: 0, 3: 0, 4: 0}

        for row in self.sheet.iter_rows(values_only=True):
            level = row[-1]
            if level in levels_count:
                levels_count[level] += 1
        for level, count in levels_count.items():
            print(f"Level {level}: {count}명")

#UserInfo().show_selected_user("user1")
#UserInfo().show_all_user()

UserInfo().show_distribution_user()
UserInfo().show_total_user_count()
            