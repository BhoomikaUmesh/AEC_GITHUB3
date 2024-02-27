def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(n):
    primes = [i for i in range(2, n+1) if is_prime(i)]
    return primes

# User input for the upper limit of prime numbers
n = int(input("Enter the upper limit to print prime numbers: "))
print(print_primes(n))
