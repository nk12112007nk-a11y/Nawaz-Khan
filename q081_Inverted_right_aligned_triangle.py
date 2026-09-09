"""
Problem 81 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Inverted right-aligned triangle
"""
def inverted_right_aligned_triangle(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
    inverted_right_aligned_triangle(5)
