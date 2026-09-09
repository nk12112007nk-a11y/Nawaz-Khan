"""
Problem 100 [Nested Loops / Inner For Loops - Patterns / Alphabet Patterns]
Reverse alphabet triangle
"""
import string

def reverse_alphabet_triangle(n):
    letters = string.ascii_uppercase
    for i in range(n, 0, -1):
        print(letters[:i])

if __name__ == "__main__":
    reverse_alphabet_triangle(5)
