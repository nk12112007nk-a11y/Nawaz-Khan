"""
Problem 88 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Number triangle (row-wise)
"""
def number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(i) for _ in range(i)))

if __name__ == "__main__":
    number_triangle(5)
