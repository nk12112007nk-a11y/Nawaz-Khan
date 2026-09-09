"""
Problem 66 [Loops / Applied / Mixed Loop Problems]
Find the sum of even and odd numbers separately from 1 to N
"""
def sum_even_odd(n):
    even_sum, odd_sum = 0, 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum

if __name__ == "__main__":
    n = 10
    e, o = sum_even_odd(n)
    print(f"Sum of even numbers 1..{n} = {e}")
    print(f"Sum of odd numbers 1..{n} = {o}")
