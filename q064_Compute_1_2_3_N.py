"""
Problem 64 [Loops / Series & Patterns (Single Loop)]
Compute: 1! + 2! + 3! + ... + N!
"""
def sum_of_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total

if __name__ == "__main__":
    n = 5
    print(f"1! + 2! + ... + {n}! = {sum_of_factorials(n)}")
