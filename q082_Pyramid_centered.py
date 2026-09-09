"""
Problem 82 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Pyramid (centered)
"""
def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    pyramid(5)
