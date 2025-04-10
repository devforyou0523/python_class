#키보드 입력 (input함수)
#num1 = input("첫번째 정수:")
#num2 = input("두번째 정수:")
#result = num1+ num2

#print ("num1 + num2 = {}".format(result)) #input은 문자열로 입력받기에, 문자열의 합으로 나타난다

num1 = int(input("첫번째 정수: "))
num2 = int(input("두번째 정수: ")) #입력된 input 값(String)을 int 값으로 변환한다. 이러한 형태 변환 작업을 Typecast, 형변환이라 한다.
result = num1+ num2

print ("num1 + num2 = {}".format(result))