dict_a = {1:1, 2:2}

def fibonacci(n):
   if n in dict_a:
    return dict_a[n]
   else:
    output = fibonacci(n-1) + fibonacci(n-2)
    dict_a[n] = output
    return output

print(f"fibonacci(10): {fibonacci(10)}")
print(f"fibonacci(20): {fibonacci(20)}")
print(f"fibonacci(30): {fibonacci(30)}")
print(f"fibonacci(40): {fibonacci(40)}")
print(f"fibonacci(50): {fibonacci(50)}")