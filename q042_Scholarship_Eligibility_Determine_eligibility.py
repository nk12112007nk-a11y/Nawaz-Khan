"""
Problem 42 [Conditional Statements / Mixed / Applied]
Scholarship Eligibility : Determine eligibility based on marks, attendance, and family income.
"""
def scholarship_eligibility(marks, attendance, family_income):
    if marks >= 75 and attendance >= 80 and family_income < 200000:
        return "Eligible for scholarship"
    return "Not eligible for scholarship"

if __name__ == "__main__":
    print(scholarship_eligibility(80, 85, 150000))
    print(scholarship_eligibility(60, 85, 150000))
    print(scholarship_eligibility(80, 85, 300000))
