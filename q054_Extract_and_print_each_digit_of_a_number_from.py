"""
Problem 54 [Loops / Digit-Based Problems]
Extract and print each digit of a number from left to right
"""
def digits_left_to_right(n):
    digits = str(abs(n))
    for d in digits:
        print(d, end=" ")
    print()

if __name__ == "__main__":
    digits_left_to_right(45678)
