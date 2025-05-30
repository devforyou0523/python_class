#문제 3 공약수 구하기
input_num1 = int(input("첫 번째 양의 정수를 입력해주세요. : ")) #두 수 입력받기
input_num2 = int(input("두 번째 양의 정수를 입력해주세요. : "))
common_divisor_list = [] #공약수 리스트 선언

def common_divisors(a, b): #공약수 계산 함수
    #a와 b의 최대 공약수는 반드시 a, b 중 작은 수보다 작거나 같다. 
    if a>=b:
        for i in range (1, b+1): 
            if a%i == 0 and b%i == 0: #a를 i로 나눈 나머지와 b를 i로 나눈 나머지가 모두 0인 경우 
                common_divisor_list.append(i) #i를 공약수 리스트에 추가
    elif a<b:
        for i in range (1, a+1): 
            if a%i == 0 and b%i == 0:
                common_divisor_list.append(i)

common_divisors(input_num1, input_num2) #입력받은 두 수로 함수 호출 
print(f">>> common_divisors({input_num1}, {input_num2}) \n {common_divisor_list}")
