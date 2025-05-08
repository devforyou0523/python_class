#반복문을 이용한 텍스트 파일 생성
import random
hanguls = "가나다라마바사아자차카타파하"

with open("list.csv", "w") as file:
    file.write("이름, 몸무게, 키\n")

    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        height = random.randrange(140, 200)
        weight = random.randrange(40, 100)

        file.write(f"{name}, {weight}, {height}\n")