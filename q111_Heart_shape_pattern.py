"""
Problem 111 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Heart shape pattern
"""
def heart_pattern(n=6):
    """Prints a heart shape using two top humps (nested loops) and an
    inverted-triangle bottom, a classic pattern-programming approach."""
    # Top two humps
    for i in range(n // 2, n, 2):
        for _ in range(1):
            row = " " * (n - i)
            row += "*" * i
            row += " " * (2 * (n - i))
            row += "*" * i
            print(row)
    # Bottom inverted triangle
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    heart_pattern(6)
