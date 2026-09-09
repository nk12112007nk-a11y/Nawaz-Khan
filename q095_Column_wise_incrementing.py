"""
Problem 95 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Column-wise incrementing
"""
def column_wise_incrementing(n):
    for i in range(1, n + 1):
        row = [str(j) for j in range(1, i + 1)]
        print(" ".join(row))

if __name__ == "__main__":
    column_wise_incrementing(5)
