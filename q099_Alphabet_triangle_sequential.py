"""
Problem 99 [Nested Loops / Inner For Loops - Patterns / Alphabet Patterns]
Alphabet triangle (sequential)
"""
import string

def alphabet_triangle_sequential(n):
    letters = string.ascii_uppercase
    for i in range(1, n + 1):
        print(letters[:i])

if __name__ == "__main__":
    alphabet_triangle_sequential(5)
