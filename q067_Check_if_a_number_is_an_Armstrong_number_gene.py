"""
Problem 67 [Loops / Applied / Mixed Loop Problems]
Check if a number is an Armstrong number (generalized for any digits)
"""
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

if __name__ == "__main__":
    for n in [153, 9474, 123]:
        print(f"{n}: {'Armstrong' if is_armstrong(n) else 'Not Armstrong'}")
