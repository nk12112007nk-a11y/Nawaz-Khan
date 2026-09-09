"""
Problem 104 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Hollow diamond inside rectangle
"""
def hollow_diamond_in_rectangle(n, width=None):
    if width is None:
        width = 2 * n
    diamond_rows = []
    for i in range(1, n + 1):
        row = " " * (n - i) + "*" * (2 * i - 1) + " " * (n - i)
        diamond_rows.append(row)
    for i in range(n - 1, 0, -1):
        row = " " * (n - i) + "*" * (2 * i - 1) + " " * (n - i)
        diamond_rows.append(row)
    for row in diamond_rows:
        print("*" + row.center(width) + "*")

if __name__ == "__main__":
    hollow_diamond_in_rectangle(4)
