"""
Problem 106 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Zigzag pattern
"""
def zigzag_pattern(rows, cols):
    matrix = [[" " for _ in range(cols)] for _ in range(rows)]
    for col in range(cols):
        row_pos = col % (2 * rows - 2)
        if row_pos >= rows:
            row_pos = 2 * rows - 2 - row_pos
        matrix[row_pos][col] = "*"
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    zigzag_pattern(4, 12)
