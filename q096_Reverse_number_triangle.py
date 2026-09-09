"""
Problem 96 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Reverse number triangle
"""
def reverse_number_triangle(n):
    for i in range(1, n + 1):
        row = [str(j) for j in range(n, n - i, -1)]
        print(" ".join(row))

if __name__ == "__main__":
    reverse_number_triangle(5)
