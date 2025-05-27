class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add (self):
        return self.a + self.b
    
    def sub (self):
        return self.a - self.b

set_1 = calc(5,10)
set_2 = calc(10, 2)

print(set_1.add())
print(set_1.sub())

print(set_2.add())
print(set_2.sub())