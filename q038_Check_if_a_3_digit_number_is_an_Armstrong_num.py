"""
Problem 38 [Conditional Statements / Mixed / Applied]
Check if a 3-digit number is an Armstrong number (e.g., 153)
"""
def is_armstrong_3digit(n):
    s = str(n)
    total = sum(int(d) ** 3 for d in s)
    return total == n

if __name__ == "__main__":
    for n in [153, 370, 123]:
        print(f"{n}: {'Armstrong' if is_armstrong_3digit(n) else 'Not Armstrong'}")
