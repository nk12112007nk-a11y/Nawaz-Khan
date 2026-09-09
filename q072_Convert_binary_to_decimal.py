"""
Problem 72 [Loops / Applied / Mixed Loop Problems]
Convert binary to decimal
"""
def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

if __name__ == "__main__":
    for b in ["1010", "11111111", "0"]:
        print(f"{b} in decimal = {binary_to_decimal(b)}")
