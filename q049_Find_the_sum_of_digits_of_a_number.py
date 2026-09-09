"""
Problem 49 [Loops / Digit-Based Problems]
Find the sum of digits of a number
"""
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    for n in [12345, 999]:
        print(f"{n}: sum of digits = {sum_of_digits(n)}")
