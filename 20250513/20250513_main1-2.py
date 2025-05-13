#예외 객체 이용
try:
    input_num = int(input())
    print(f"input_num is {input_num}")
except Exception as e: #예외 객체 Exception을 e로 취급함
    print(f"Error is: {e}\nError type is {type(e)}")