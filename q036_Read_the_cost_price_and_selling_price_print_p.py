"""
Problem 36 [Conditional Statements / Mixed / Applied]
Read the cost price and selling price — print profit, loss, or no profit no loss
"""
def profit_loss(cp, sp):
    if sp > cp:
        return f"Profit of {sp - cp}"
    elif sp < cp:
        return f"Loss of {cp - sp}"
    else:
        return "No profit no loss"

if __name__ == "__main__":
    print(profit_loss(100, 120))
    print(profit_loss(150, 100))
    print(profit_loss(100, 100))
