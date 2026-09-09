"""
Problem 50 [Loops / Digit-Based Problems]
Reverse a number
"""
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev

if __name__ == "__main__":
    for n in [12345, -678]:
        print(f"{n}: reversed = {reverse_number(n)}")
