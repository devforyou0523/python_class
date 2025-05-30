#문제 1 알파벳 개수 세기
input_string = input().lower() #대.소문자 중복 감지를 위한 소문자 변환
alphabet_dict = {} #알파벳 딕셔너리

for char in input_string: #입력받은 문자열의 길이만큼 반복하는 for문
    if char.isalpha() : #현재 for문에서 작동중인 문자열이 알파벳인지 검사
            if char in alphabet_dict: #현재 for문에서 작동중인 문자열이 알파벳 딕셔너리에 있는 경우
                alphabet_dict[char] = alphabet_dict[char] + 1 #기존 딕셔너리의 벨류 값에서 1 증가
            else: #현재 for문에서 작동중인 문자열이 알파벳 딕셔너리에 없는 경우
                alphabet_dict[char] = 1 #초기 딕셔너리 값 1 배정
    else: #알파벳이 아닌경우 다음 문자열로 넘김
         pass

print(alphabet_dict)