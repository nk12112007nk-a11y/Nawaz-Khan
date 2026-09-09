"""
Problem 40 [Conditional Statements / Mixed / Applied]
ATM Withdrawal : Approve or reject a withdrawal based on amount, balance, and minimum-balance rules.
"""
def atm_withdrawal(amount, balance, min_balance=500):
    if amount <= 0:
        return "Invalid withdrawal amount"
    if amount % 100 != 0:
        return "Amount must be in multiples of 100"
    if balance - amount < min_balance:
        return "Rejected: Insufficient balance (minimum balance rule)"
    return f"Approved: Withdraw {amount}. New balance = {balance - amount}"

if __name__ == "__main__":
    print(atm_withdrawal(1000, 2000))
    print(atm_withdrawal(1900, 2000))
    print(atm_withdrawal(150, 2000))
