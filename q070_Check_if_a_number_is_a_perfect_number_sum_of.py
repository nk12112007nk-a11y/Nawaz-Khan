"""
Problem 70 [Loops / Applied / Mixed Loop Problems]
Check if a number is a perfect number (sum of divisors == number)
"""
def is_perfect_number(n):
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

if __name__ == "__main__":
    for n in [6, 28, 12]:
        print(f"{n}: {'Perfect number' if is_perfect_number(n) else 'Not perfect'}")
