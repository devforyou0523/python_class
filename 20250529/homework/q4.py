#문제 4 숫자 말 바꾸기 게임
for i in range (1, 100+1): #1부터 100까지 범위 설정
    if i%3 == 0 and i%5 == 0: #i가 3과 5로 동시에 나누어떨어지는 경우, 이는 3과 5의 공배수이다.
        print("FizzBuzz")
    elif i%3 == 0: #i가 3으로 나누어떨어지는 경우
        print("Fizz")
    elif i%5 == 0: #i가 5로 나누어떨어지는 경우
        print("Buzz")
    else: #i가 3과 5 둘 중 어느것으로도 나누어떨어지지 않는 경우
        print(i)