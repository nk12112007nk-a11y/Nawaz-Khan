"""
Problem 103 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Butterfly pattern
"""
def butterfly_pattern(n):
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

if __name__ == "__main__":
    butterfly_pattern(5)
