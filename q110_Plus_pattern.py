"""
Problem 110 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Plus (+) pattern
"""
def plus_pattern(n):
    mid = n // 2
    for i in range(n):
        row = ""
        for j in range(n):
            if i == mid or j == mid:
                row += "*"
            else:
                row += " "
        print(row)

if __name__ == "__main__":
    plus_pattern(5)
