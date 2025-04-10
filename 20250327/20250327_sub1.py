input_list = input().split(" ") #입력받은 원소 분리 (List형으로 반환)
input_list_length = len(input_list) #초기 List의 길이
edited_list = [] #새로운 List

for i in range(input_list_length): #초기 List의 길이만큼 원소를 int형으로 바꿈
    edited_list = edited_list.__add__([int(input_list[i])]) #바꾼 int형의 원소를 새 List에 포함함
    #print("i: {}".format(i))
    #print(edited_list)
    if (i == input_list_length-1): #초기 List의 길이만큼 반복이 끝났을때 
        print("final edited_list: {}".format(edited_list)) #새 List 출력
        print("final edited_list[0] type: {}".format(type(edited_list[0]))) #새 List의 0번째 원소 Type 출력