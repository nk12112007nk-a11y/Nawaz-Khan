"""
Problem 63 [Loops / Series & Patterns (Single Loop)]
Find x^n (power) without using built-in pow function
"""
def power(x, n):
    result = 1
    for _ in range(abs(n)):
        result *= x
    if n < 0:
        return 1 / result
    return result

if __name__ == "__main__":
    print(f"2^10 = {power(2, 10)}")
    print(f"5^0 = {power(5, 0)}")
    print(f"2^-3 = {power(2, -3)}")
