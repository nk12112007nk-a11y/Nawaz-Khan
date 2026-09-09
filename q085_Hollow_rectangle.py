"""
Problem 85 [Nested Loops / Inner For Loops - Patterns / Star Patterns]
Hollow rectangle
"""
def hollow_rectangle(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i == 1 or i == rows or j == 1 or j == cols:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    hollow_rectangle(5, 8)
