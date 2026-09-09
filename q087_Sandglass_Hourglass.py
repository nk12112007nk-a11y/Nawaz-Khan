"""
Problem 87 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Sandglass / Hourglass
"""
def hourglass(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    hourglass(5)
