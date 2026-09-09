"""
Problem 68 [Loops / Applied / Mixed Loop Problems]
Find the largest and smallest digit in a number
"""
def largest_smallest_digit(n):
    n = abs(n)
    digits = [int(d) for d in str(n)]
    return max(digits), min(digits)

if __name__ == "__main__":
    n = 5273891
    largest, smallest = largest_smallest_digit(n)
    print(f"{n}: largest digit = {largest}, smallest digit = {smallest}")
