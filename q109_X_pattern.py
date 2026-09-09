"""
Problem 109 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
X pattern
"""
def x_pattern(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if j == i or j == (n - 1 - i):
                row += "*"
            else:
                row += " "
        print(row)

if __name__ == "__main__":
    x_pattern(5)
