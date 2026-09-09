"""
Problem 39 [Conditional Statements / Mixed / Applied]
Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5× rate)
"""
def compute_salary(hours, rate):
    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        return regular + overtime
    return hours * rate

if __name__ == "__main__":
    print(f"Salary: {compute_salary(45, 20)}")
    print(f"Salary: {compute_salary(35, 20)}")
