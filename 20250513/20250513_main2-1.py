#인라인 람다
input_list_a = [1,2,3,4,5]

output_a = map(lambda x: x*x, input_list_a)
print("#map() 함수 실행결과")

print(f"map(power, input_list_a): {output_a}")
print(f"map(power, input_list_a): {list(output_a)}")
print()

output_b = filter(lambda x: x<3, input_list_a)
print("#filter() 함수 실행결과")

print(f"filter(filter, input_list_a): {output_b}")
print(f"filter(filter, input_list_a): {list(output_b)}")
print()