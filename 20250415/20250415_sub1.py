#리스트 최저 원소 찾기
list_a = [14467, 12, 42, 1, 12, 134, 1452, 23]
min_number = list_a[0]

for i in range(len(list_a)):
    print(f"검사대상은 {list_a[i]}입니다.")
    for j in range(len(list_a)):
        print(f"검사대상은 {list_a[i]}, 비교대상은 {min_number} 입니다.")
        if list_a[j] == min_number:
            print(f"검사대상과 비교대상이 같습니다. 검사대상이 최저숫자입니다. 다음 비교대상으로 넘어갑니다. 현재 최저숫자는 {min_number} 입니다.")
            min_number = list_a[j]
        elif list_a[j] < min_number:
            print(f"검사대상이 비교대상보다 작습니다. 검사대상이 최저숫자입니다. 다음 비교대상으로 넘어갑니다. 현재 최저숫자는 {min_number} 입니다.")
            min_number = list_a[j]
        elif list_a[j] > min_number:
            print(f"검사대상이 비교대상보다 큽니다. 다음 검사대상으로 넘어갑니다. 현재 최저숫자는 {min_number} 입니다.")
            break
print(f"리스트 내부 최저 숫자는 {min_number} 입니다.")