class User:
    def __init__(self, id, password, name, role, level):
        self.id = id
        self.password = password
        self.name = name
        self.role = role
        self.level = level

    def id(self):
        return self.id
    
    def password(self):
        return self.password
    
    def name(self):
        return self.name
    
    def role(self):
        return self.role
    
    def level(self):
        return self.level
        