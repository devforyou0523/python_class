class Member:
    global members
    members = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def register (self):
        members[len(members)] = {self.name : self.age}
    def returnMember (self):
        return members

for i in range(1, int(input("가입자 인원을 입력해주세요: "))+1):
    name, age = input(f"{i}번째 회원의 이름과 나이를 공백으로 구분하여 입력해주세요 : ").split(" ")
    age = int(age)

    member = Member(name, age)
    member.register()

print(member.returnMember())