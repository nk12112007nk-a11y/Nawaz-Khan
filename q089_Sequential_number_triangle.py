"""
Problem 89 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Sequential number triangle
"""
def sequential_number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

if __name__ == "__main__":
    sequential_number_triangle(5)
