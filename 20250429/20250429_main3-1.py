#피보나치 계산 횟수
counter = 0

def fibonacci(n):
    print(f"피보나치 {n}")
    global counter
    counter +=1

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(10)
print(f"---\n계산횟수: {counter}")