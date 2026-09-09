"""
Problem 47 [Loops / Basic Counting & Iteration]
Calculate the sum of first N natural numbers
"""
def sum_first_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = 10
    print(f"Sum of first {n} natural numbers = {sum_first_n(n)}")
