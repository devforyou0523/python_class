#예외 처리
try:
    input_num = int(input("정수 입력>>"))
    print(f"원의 반지름: {input_num}")
    print(f"원의 둘레: {input_num*2*3.14}")
    print(f"원의 넓이: {input_num*3.14*input_num}")
except:
    print("정수를 입력해야 합니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")