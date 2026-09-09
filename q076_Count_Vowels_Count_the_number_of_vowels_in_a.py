"""
Problem 76 [Loops / Applied / Mixed Loop Problems]
Count Vowels: Count the number of vowels in a string using recursion.
"""
def count_vowels(s, index=0):
    if index >= len(s):
        return 0
    is_vowel = 1 if s[index].lower() in "aeiou" else 0
    return is_vowel + count_vowels(s, index + 1)

if __name__ == "__main__":
    for s in ["hello world", "programming"]:
        print(f"'{s}': {count_vowels(s)} vowels")
