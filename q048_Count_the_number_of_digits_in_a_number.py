"""
Problem 48 [Loops / Digit-Based Problems]
Count the number of digits in a number
"""
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

if __name__ == "__main__":
    for n in [12345, 7, 0]:
        print(f"{n}: {count_digits(n)} digits")
