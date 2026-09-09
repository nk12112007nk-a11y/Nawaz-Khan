"""
Problem 98 [Nested Loops / Inner For Loops - Patterns / Alphabet Patterns]
Alphabet triangle (row repeat)
"""
import string

def alphabet_triangle_row_repeat(n):
    letters = string.ascii_uppercase
    for i in range(1, n + 1):
        print(letters[i - 1] * i)

if __name__ == "__main__":
    alphabet_triangle_row_repeat(5)
