"""
Problem 101 [Nested Loops / Inner For Loops - Patterns / Alphabet Patterns]
Right-aligned alphabet triangle
"""
import string

def right_aligned_alphabet_triangle(n):
    letters = string.ascii_uppercase
    for i in range(1, n + 1):
        print(" " * (n - i) + letters[:i])

if __name__ == "__main__":
    right_aligned_alphabet_triangle(5)
