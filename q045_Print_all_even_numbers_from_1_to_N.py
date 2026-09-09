"""
Problem 45 [Loops / Basic Counting & Iteration]
Print all even numbers from 1 to N
"""
def print_evens(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

if __name__ == "__main__":
    print_evens(20)
