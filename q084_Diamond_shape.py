"""
Problem 84 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Diamond shape
"""
def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    diamond(5)
