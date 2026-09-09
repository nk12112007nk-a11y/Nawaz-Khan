"""
Problem 107 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Spiral number matrix (4×4)
"""
def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix

if __name__ == "__main__":
    for row in spiral_matrix(4):
        print(" ".join(f"{v:2d}" for v in row))
