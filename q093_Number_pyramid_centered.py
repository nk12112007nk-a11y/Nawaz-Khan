"""
Problem 93 [Nested Loops / Inner For Loops - Patterns / Number Patterns]
Number pyramid (centered)
"""
def number_pyramid(n):
    for i in range(1, n + 1):
        spaces = " ".join(str(i) for _ in range(i))
        print(spaces.center(n * 3))

if __name__ == "__main__":
    number_pyramid(5)
