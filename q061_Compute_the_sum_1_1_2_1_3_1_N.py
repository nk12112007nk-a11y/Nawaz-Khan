"""
Problem 61 [Loops / Series & Patterns (Single Loop)]
Compute the sum: 1 + 1/2 + 1/3 + ... + 1/N
"""
def harmonic_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1 / i
    return total

if __name__ == "__main__":
    n = 5
    print(f"Sum 1 + 1/2 + ... + 1/{n} = {harmonic_sum(n):.4f}")
