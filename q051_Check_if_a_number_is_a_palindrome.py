"""
Problem 51 [Loops / Digit-Based Problems]
Check if a number is a palindrome
"""
def is_palindrome_number(n):
    original = n
    return original == reverse_number(n)

def reverse_number(n):
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

if __name__ == "__main__":
    for n in [121, 12345]:
        print(f"{n}: {'Palindrome' if is_palindrome_number(n) else 'Not palindrome'}")
