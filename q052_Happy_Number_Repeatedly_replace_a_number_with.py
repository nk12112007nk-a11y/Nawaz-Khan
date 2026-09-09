"""
Problem 52 [Loops / Digit-Based Problems]
Happy Number: Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1.
"""
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

if __name__ == "__main__":
    for n in [19, 2, 7]:
        print(f"{n}: {'Happy' if is_happy_number(n) else 'Not happy'}")
