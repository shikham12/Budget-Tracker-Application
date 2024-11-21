def SavingsGoalTracker(goal_amount, savings, months_to_goal):
    total_savings = savings * months_to_goal
    progress = (total_savings / goal_amount) * 100 if goal_amount > 0 else 0
    remaining_amount = goal_amount - total_savings

    return progress, remaining_amount