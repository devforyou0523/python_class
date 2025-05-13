#예외처리 return 구문
def test():
    print("test 함수 시작")

    try:
        print("try구문 실행 시작")
        return
        print("try 구문의 return 뒤")
    except:
        print("except 구문 실행 시작")
    else:
        print("else 구문 실행 시작")
    finally:
        print("finally 구문 실행 시작")
    print("test 함수 끝")

test()