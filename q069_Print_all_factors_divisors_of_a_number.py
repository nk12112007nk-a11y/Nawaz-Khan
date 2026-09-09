"""
Problem 69 [Loops / Applied / Mixed Loop Problems]
Print all factors / divisors of a number
"""
def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    n = 36
    print(f"Factors of {n}: {factors(n)}")
