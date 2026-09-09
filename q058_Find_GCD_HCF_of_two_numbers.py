"""
Problem 58 [Loops / Math / Number Theory]
Find GCD / HCF of two numbers
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a, b = 36, 60
    print(f"GCD of {a} and {b} = {gcd(a, b)}")
