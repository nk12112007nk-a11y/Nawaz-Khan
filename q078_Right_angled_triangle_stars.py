"""
Problem 78 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Right-angled triangle (stars)
"""
def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == "__main__":
    right_triangle(5)
