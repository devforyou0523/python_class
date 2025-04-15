list_a = ["요소1", "요소2", "요소3"]

print(list_a)

print(enumerate(list_a))

print(list(enumerate(list_a)))

for i, value in enumerate(list_a):
    print(f"{i}번째 요소는 {value}입니다.")