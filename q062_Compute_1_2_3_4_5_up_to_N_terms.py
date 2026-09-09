"""
Problem 62 [Loops / Series & Patterns (Single Loop)]
Compute: 1 − 2 + 3 − 4 + 5 − ... up to N terms
"""
def alternating_sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i
        else:
            total -= i
    return total

if __name__ == "__main__":
    n = 6
    print(f"1 - 2 + 3 - 4 + ... up to {n} terms = {alternating_sum(n)}")
