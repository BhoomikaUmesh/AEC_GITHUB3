def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# User input for the number to calculate factorial
n = int(input("Enter a number to calculate its factorial: "))
print(factorial(n))
