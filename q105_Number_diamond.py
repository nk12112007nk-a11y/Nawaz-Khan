"""
Problem 105 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Number diamond
"""
def number_diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(i) for _ in range(2 * i - 1)))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + " ".join(str(i) for _ in range(2 * i - 1)))

if __name__ == "__main__":
    number_diamond(4)
