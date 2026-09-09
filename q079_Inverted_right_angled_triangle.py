"""
Problem 79 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Inverted right-angled triangle
"""
def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)

if __name__ == "__main__":
    inverted_right_triangle(5)
