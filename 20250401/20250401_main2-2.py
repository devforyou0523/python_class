#in 조건문
number = input("정수 입력> ")
last_char = number[-1]
last_number = int(last_char)

if last_char in "02468":
    print("짝수입니다.")

if last_char in "13579":
    print("홀수입니다.")