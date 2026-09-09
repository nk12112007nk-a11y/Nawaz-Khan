"""
Problem 53 [Loops / Digit-Based Problems]
Product of Digits: Find the product of all digits of a number using recursion.
"""
def product_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

if __name__ == "__main__":
    for n in [234, 5, 109]:
        print(f"{n}: product of digits = {product_of_digits(n)}")
