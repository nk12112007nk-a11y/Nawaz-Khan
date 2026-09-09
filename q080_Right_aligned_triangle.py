"""
Problem 80 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Right-aligned triangle
"""
def right_aligned_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
    right_aligned_triangle(5)
