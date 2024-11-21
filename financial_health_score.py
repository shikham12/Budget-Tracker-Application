def FinancialHealthScore(income, expenses, savings):
    if income == 0:
        return 0  # Avoid division by zero

    # Calculate savings rate
    savings_rate = (savings / income) * 100

    # Calculate expense ratio
    expense_ratio = (expenses / income) * 100

    # Calculate financial health score
    score = savings_rate - expense_ratio

    # Normalize score to be between 0 and 100
    score = max(0, min(score, 100))

    return score