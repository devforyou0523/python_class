number = input("정수 입력> ")
last_char = number[-1]
last_number = int(last_char)

if (last_char == 0 | last_char == 2 | last_char == 4 | last_char == 6 | last_char == 8 ):
    print("짝수입니다.")
if (last_char == 1 | last_char == 3 | last_char == 5 | last_char == 7 | last_char == 9 ):
    print("홀수입니다.")