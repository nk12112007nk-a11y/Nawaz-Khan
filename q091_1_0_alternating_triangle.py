"""
Problem 91 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
1-0 alternating triangle
"""
def alternating_1_0_triangle(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append("1" if (i + j) % 2 == 0 else "0")
        print(" ".join(row))

if __name__ == "__main__":
    alternating_1_0_triangle(5)
