#일반 매개변수, 가변 매개변수
def print_n_times (value, n=2, *added_value):
    for i in range(n):
        print(value, added_value)


#print_n_times("hello", 3, 1, 2, 3)