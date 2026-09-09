"""
Problem 55 [Loops / Math / Number Theory]
Find factorial of N
"""
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    for n in [5, 0, 10]:
        print(f"{n}! = {factorial(n)}")
