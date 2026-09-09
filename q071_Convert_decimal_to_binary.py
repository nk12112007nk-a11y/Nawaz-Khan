"""
Problem 71 [Loops / Applied / Mixed Loop Problems]
Convert decimal to binary
"""
def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = ""
    num = abs(n)
    while num > 0:
        bits = str(num % 2) + bits
        num //= 2
    return ("-" if n < 0 else "") + bits

if __name__ == "__main__":
    for n in [10, 255, 0]:
        print(f"{n} in binary = {decimal_to_binary(n)}")
