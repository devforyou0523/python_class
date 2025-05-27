def create_student (name, korean, math, english, science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def student_get_sum (student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_avg (student):
    return (student_get_sum(student) /4)

def student_to_str (student):
    return f"{student["name"]}\t {student_get_sum(student)}\t {student_get_avg(student)}\t"

students = [create_student("윤인성", 32, 49, 94, 85),
            create_student("연하진", 42, 76, 56, 74),
            create_student("구지연", 54, 56, 76, 56),
            create_student("나선주", 32, 86, 64, 37),
            create_student("윤아린", 23, 54, 74, 37),
            create_student("윤명월", 56, 66, 73, 34),
            ]

print("이름 총점 평균\n")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    print(f"{student["name"]} {score_sum} {score_sum/4}")