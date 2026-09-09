"""
Problem 102 [Nested Loops / Inner For Loops - Patterns / Alphabet Patterns]
Alphabet pyramid (centered)
"""
import string

def alphabet_pyramid(n):
    letters = string.ascii_uppercase
    for i in range(1, n + 1):
        row = letters[:i]
        print(" ".join(row).center(n * 3))

if __name__ == "__main__":
    alphabet_pyramid(5)
