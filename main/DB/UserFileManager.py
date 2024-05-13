import os
from openpyxl import load_workbook

cwd = os.getcwd()

user_file_path = f"{cwd}\\main\\DB\\UserList.xlsx"

wb = load_workbook(user_file_path)


def userExists(userId):
    if(userId):
        #엑셀에서 userId가 있는지 확인한다.
        return True
    else:
        return False

def getUserPassword(userId):
    # 엑셀에서 유저의 패스워드를 가져온다.
    if(userId):
        pass

    # 해당 유저가 없는 경우
    else:
        return False

# 해당 유저의 레벨을 가져온다.
def getUserLevel(userId):
    pass


# 전체 유저의 점수대별 분포를 보여준다.
def getDist():
    pass