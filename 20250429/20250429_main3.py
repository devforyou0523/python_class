#피보나치 수열
def fibonacci (n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(f"fibonacci(1): {fibonacci(1)}")
print(f"fibonacci(2): {fibonacci(2)}")
print(f"fibonacci(3): {fibonacci(3)}")
print(f"fibonacci(4): {fibonacci(4)}")
print(f"fibonacci(5): {fibonacci(5)}")