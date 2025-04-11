#format의 다양한 사용법
string_a = "{}".format(10)

print(string_a)
print(type(string_a))

format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)
format_d = "{} {} {}".format(1, "문자열", True)


#출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)