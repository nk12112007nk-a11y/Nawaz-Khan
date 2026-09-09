"""
Problem 108 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Right arrow pattern
"""
def right_arrow_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
    right_arrow_pattern(5)
