#팩토리얼 만들기
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)
    # output = 1
    # for i in range (1, n+1):
    #     output = output * i
    # return output

print(f"1!: {factorial(1)}")
print(f"2!: {factorial(2)}")
print(f"3!: {factorial(3)}")
print(f"4!: {factorial(4)}")
print(f"5!: {factorial(5)}")