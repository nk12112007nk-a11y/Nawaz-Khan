"""
Problem 60 [Loops / Series & Patterns (Single Loop)]
Print Fibonacci series up to N terms
"""
def fibonacci(n_terms):
    fib = []
    a, b = 0, 1
    for _ in range(n_terms):
        fib.append(a)
        a, b = b, a + b
    return fib

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci series ({n} terms): {fibonacci(n)}")
