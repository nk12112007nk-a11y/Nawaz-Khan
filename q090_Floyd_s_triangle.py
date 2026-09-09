"""
Problem 90 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Floyd's triangle
"""
def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

if __name__ == "__main__":
    floyds_triangle(5)
