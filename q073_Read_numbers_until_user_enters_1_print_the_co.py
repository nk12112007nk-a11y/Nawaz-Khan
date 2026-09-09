"""
Problem 73 [Loops / Applied / Mixed Loop Problems]
Read numbers until user enters −1, print the count and average
"""
def read_until_negative_one(numbers):
    """numbers: a list simulating sequential user input, ending logic stops at -1."""
    count = 0
    total = 0
    for num in numbers:
        if num == -1:
            break
        count += 1
        total += num
    if count == 0:
        return 0, 0
    return count, total / count

if __name__ == "__main__":
    sample_input = [10, 20, 30, 40, -1]
    count, avg = read_until_negative_one(sample_input)
    print(f"Input sequence: {sample_input}")
    print(f"Count = {count}, Average = {avg}")
