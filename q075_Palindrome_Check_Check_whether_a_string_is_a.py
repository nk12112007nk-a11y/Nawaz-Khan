"""
Problem 75 [Loops / Applied / Mixed Loop Problems]
Palindrome Check: Check whether a string is a palindrome using recursion
"""
def is_palindrome_string(s, i=0, j=None):
    if j is None:
        j = len(s) - 1
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_palindrome_string(s, i + 1, j - 1)

if __name__ == "__main__":
    for s in ["madam", "hello", "racecar"]:
        print(f"'{s}': {'Palindrome' if is_palindrome_string(s) else 'Not palindrome'}")
