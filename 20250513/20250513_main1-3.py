#예외 상황 구분
num_list = [52, 273, 32, 72, 100]

try:
    input_num = int(input("정수 입력: "))

    print(f"{input_num}번째 요소: {num_list[input_num-1]}")

except ValueError:
    print("정수를 입력해주세요")
except IndexError:
    print("리스트 인덱스 초과")
