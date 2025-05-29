class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def student_get_sum (self):
        return self.korean + self.math + self.english + self.science
    
    def student_get_avg (self):
        return (self.korean + self.math + self.english + self.science) /4
    
    def student_to_string (self):
        return f"{self.name} {self.student_get_sum()} {self.student_get_avg()}"

students = [
    Student("윤인성", 32, 49, 94, 85),
    Student("연하진", 42, 76, 56, 74),
    Student("구지연", 54, 56, 76, 56),
    Student("나선주", 32, 86, 64, 37),
    Student("윤아린", 23, 54, 74, 37),
    Student("윤명월", 56, 66, 73, 34),
]

for i in students:
    print(i.student_to_string())