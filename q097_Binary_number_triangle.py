"""
Problem 97 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Binary number triangle
"""
def binary_number_triangle(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append("1" if j % 2 != 0 else "0")
        print(" ".join(row))

if __name__ == "__main__":
    binary_number_triangle(5)
