import openai
def simulate_insight(user_data, query):
    return "Simulated Insight: Based on your expenses, you are saving well. Consider allocating more to investments."

def get_budget_insight(user_data, query):
    prompt = f"""
    You are a financial assistant. Analyze the following user data and provide insights or recommendations:

    User Data:
    - Income: {user_data['income']}
    - Expenses: {user_data['expenses']}
    - Savings: {user_data['savings']}
    - Financial Goals: {user_data.get('goal', 'Not specified')}

    User Query: {query}

    Provide a detailed and personalized response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are a financial assistant."},
            {"role": "user", "content": "Analyze my financial data and provide insights."}
            ],
            max_tokens=100,  # Use fewer tokens
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
