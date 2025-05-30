#문제 2 좌석 예약 시스템 만들기
seats_list = ["O" for i in range (10)] #초기 10개의 예약 가능 좌석 생성
reserve_num = 0

def show_seats ():
    print(f"\n현재 좌석 상태: \n {str(seats_list)[1:-1].replace("\'", "").replace(",", "")}") #리스트를 문자열로 바꾸어 출력

def reserve_seats (seat_num): #인수로 넘겨받은 수가 좌석 리스트에 있는 값인지 구분
    if seats_list[seat_num-1] == "O":
        seats_list[seat_num-1] = "X" #없던 값이면 예약을 하고, 예약 가능 상태를 X로 변경
        print(f"{seat_num}번 좌석이 예약 완료되었습니다.")

    elif seats_list[seat_num-1] == "X": #있는 값이면 예약 불가 메시지 출력
        print(f"{seat_num}번 좌석은 이미 예약되어있습니다. 다른 좌석을 선택해주세요.")

while input("\n좌석 예약을 진행하겠습니까? \n계속 예약은 1을, 종료는 1을 제외한 숫자를 눌러주세요 : ") == "1": #종료하기 전까지 반복해서 예약할 좌석 입력
    show_seats() #현재 좌석 상태 출력
    reserve_num = int(input("예약할 좌석 번호를 입력해주세요 : "))
    reserve_seats(reserve_num) #입력한 좌석번호를 인수로 넘겨주며 reserve_seats 함수를 통한 좌석 예약

print("프로그램을 종료합니다.")
        