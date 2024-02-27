def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# User input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))

