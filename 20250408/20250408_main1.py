#list 선언
list_a = [1, 2, 3]

#list에 값 추가
print("#list에 값 추가")
list_a.append(4)
list_a.append(5)
print(list_a) # [1, 2, 3, 4, 5]
print()

#list중간에 값 추가
print("#list중간에 값 추가")
list_a.insert(0,10)
print(list_a) # [10, 1, 2, 3, 4, 5]
print()

#list에 값 삭제 (del)
print("#list에 값 삭제")
del list_a[1]
print(list_a) # [10, 2, 3, 4, 5]
print()

#list에 값 삭제 (pop)
print("#list에 값 삭제 (pop)")
list_a.pop(2)
print(list_a) # [10, 2, 3, 5]
print()