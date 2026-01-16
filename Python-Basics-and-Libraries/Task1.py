def func1(n):
    print(f"Func1 received: {n}")
    return func2(n * 2)

def func2(x):
    print(f"Func2 received: {x}")
    return func3(x + 10)

def func3(y):
    print(f"Func3 received: {y}")
    result = 1
    for i in range(1, int(y) + 1):
        result *= i
    return f"Factorial: {result}"

# Run it
print(func1(5))
