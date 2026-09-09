"""
Problem 92 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Pascal's triangle
"""
def pascals_triangle(n):
    for i in range(n):
        val = 1
        row = []
        for j in range(i + 1):
            row.append(str(val))
            val = val * (i - j) // (j + 1)
        print(" ".join(row).center(n * 4))

if __name__ == "__main__":
    pascals_triangle(6)
