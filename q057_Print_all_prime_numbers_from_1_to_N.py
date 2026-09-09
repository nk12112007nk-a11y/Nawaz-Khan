"""
Problem 57 [Loops / Math / Number Theory]
Print all prime numbers from 1 to N
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

if __name__ == "__main__":
    n = 30
    print(f"Primes up to {n}: {primes_up_to(n)}")
