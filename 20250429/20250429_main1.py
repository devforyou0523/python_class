#함수 return 사용
def sum_all(x, y):
    output = 0
    for i in range (x, y+1):
        output += i
    return output

print(f"0 to 100: {sum_all(0, 100)}")
print(f"0 to 1000: {sum_all(0, 1000)}")
print(f"50 to 100: {sum_all(50, 100)}")
print(f"500 to 1000: {sum_all(500, 1000)}")