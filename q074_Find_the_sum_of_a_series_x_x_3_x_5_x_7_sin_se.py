"""
Problem 74 [Loops / Applied / Mixed Loop Problems]
Find the sum of a series: x − x³/3! + x⁵/5! − x⁷/7! ... (sin series)
"""
def sin_series(x, n_terms=10):
    total = 0.0
    term = x
    sign = 1
    for i in range(n_terms):
        power = 2 * i + 1
        fact = 1
        for j in range(1, power + 1):
            fact *= j
        total += sign * (x ** power) / fact
        sign *= -1
    return total

if __name__ == "__main__":
    import math
    x = math.pi / 6
    print(f"sin({x:.4f}) approx = {sin_series(x):.6f}")
    print(f"math.sin({x:.4f})   = {math.sin(x):.6f}")
