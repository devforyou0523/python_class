#함수 선언, 실행
def print_3_times ():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

def sum (x, y):
    res = x + y
    return res

def print_n_times (print_string, n):
    for i in range (n):
        print(print_string)
#print_3_times()
#print(sum(5,10))
print_n_times("안녕하세요", 5)
