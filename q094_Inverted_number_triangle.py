"""
Problem 94 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Inverted number triangle
"""
def inverted_number_triangle(n):
    for i in range(n, 0, -1):
        print(" ".join(str(i) for _ in range(i)))

if __name__ == "__main__":
    inverted_number_triangle(5)
