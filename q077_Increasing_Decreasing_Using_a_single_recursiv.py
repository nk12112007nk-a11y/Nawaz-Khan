"""
Problem 77 [Loops / Applied / Mixed Loop Problems]
Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order.
"""
def print_inc_dec(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_inc_dec(n, current + 1)
    print(current, end=" ")

if __name__ == "__main__":
    print("Increasing then decreasing (1..5..1):")
    print_inc_dec(5)
    print()
