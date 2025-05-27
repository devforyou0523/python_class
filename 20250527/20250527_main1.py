students = [ {"name" : "윤인성", "korean" : 24, "math" : 12, "english" : 23, "science" : 54},
             {"name" : "연하진", "korean" : 67, "math" : 64, "english" : 54, "science" : 36},
             {"name" : "구지연", "korean" : 92, "math" : 95, "english" : 56, "science" : 45}, 
             {"name" : "나선주", "korean" : 39, "math" : 54, "english" : 74, "science" : 34}, 
             {"name" : "윤아린", "korean" : 25, "math" : 93, "english" : 53, "science" : 32}, 
             {"name" : "윤명월", "korean" : 65, "math" : 62, "english" : 43, "science" : 94}, 
             ]

print("이름 총점 평균\n")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    print(f"{student["name"]} {score_sum} {score_sum/4}")