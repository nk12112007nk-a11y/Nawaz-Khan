"""
Problem 65 [Loops / Applied / Mixed Loop Problems]
Print the multiplication table of a given number
"""
def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    multiplication_table(7)
