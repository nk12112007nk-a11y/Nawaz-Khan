"""
Problem 59 [Loops / Math / Number Theory]
Find LCM of two numbers
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == "__main__":
    a, b = 4, 6
    print(f"LCM of {a} and {b} = {lcm(a, b)}")
