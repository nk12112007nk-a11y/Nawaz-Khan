"""
Problem 112 [Nested Loops / Inner For Loops - Patterns / Advanced Patterns (Nested Logic)]
Square with diagonals marked
"""
def square_with_diagonals(n):
    for i in range(n):
        row = ""
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
                row += "*"
            else:
                row += " "
        print(row)

if __name__ == "__main__":
    square_with_diagonals(7)
