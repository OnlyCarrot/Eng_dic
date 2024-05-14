from openpyxl import load_workbook

class Sheet:
    def __init__(self, sheet):
        if(sheet == "usersheet"):
            self.workbook = load_workbook("main/DB/UserList.xlsx")
            self.worksheet = self.workbook[sheet]
        else:
            self.workbook = load_workbook("main/DB/WordList.xlsx")
            self.worksheet = self.workbook[sheet]
    
    def workbook(self):
        return self.workbook
    
    def worksheet(self):
        return self.worksheet
    
        
    

