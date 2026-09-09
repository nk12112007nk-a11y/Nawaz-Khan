"""
Problem 43 [Loops / Basic Counting & Iteration]
Print numbers from 1 to N
"""
def print_1_to_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    print_1_to_n(10)
