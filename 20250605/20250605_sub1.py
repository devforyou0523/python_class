class account:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def returnAge (self):
        return self.age
    
    def returnName (self):
        return self.name
    
    def returnColor (self):
        return self.color
    
account_1 = account("Tom", 23, "Blue")
account_2 = account("Amy", 25, "Green")

print(account_1.name)