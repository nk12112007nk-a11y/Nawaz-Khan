"""
Problem 56 [Loops / Math / Number Theory]
Check if a number is prime
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for n in [7, 10, 1, 2]:
        print(f"{n}: {'Prime' if is_prime(n) else 'Not prime'}")
