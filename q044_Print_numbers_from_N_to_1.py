"""
Problem 44 [Loops / Basic Counting & Iteration]
Print numbers from N to 1
"""
def print_n_to_1(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    print_n_to_1(10)
