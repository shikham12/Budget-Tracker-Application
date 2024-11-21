# Budget Tracker Analysis Application

OVERVIEW:
This project is a Budget Tracker Analysis Application that helps users manage their financial health by tracking income, expenses, and savings.
It provides insights into their financial status, tracks savings goals, and performs budget analysis to make smarter financial decisions.
The application integrates AI-powered budget insights for personalized financial advice and features a Financial Health Score and Savings Goal Tracker to help users achieve their financial objectives.
The project is designed with a user-friendly interface, backed by a simple SQLite database for storing and retrieving financial data.

FEATURES:
1. User-Specific Budget Tracker
   - Users can add and manage categories like income, expenses, and savings.
   - The app allows users to track amounts spent, saved, or earned in each category.
   - Supports monthly financial tracking, helping users monitor their spending habits.

2. AI-Powered Budget Insight Assistant(Simulated currently)
   - Personalized insights based on the user's spending and savings habits.
   - Simulated AI responses that provides simple insights.
   
3. Financial Health Score
   - A feature that assesses the user's financial health based on their income and expenses.
   - Financial health score helps users understand if they are in a good financial position or need to adjust their habits.
   - Feedbacks are provided based on the score.

4. Savings Goal Tracker
   - Users can set and track savings goals for various purposes (e.g., emergency fund, vacation, buying a house).
   - The app calculates and displays the goal achievement percentage, motivating users to save more.
   - It uses a goal amount formula that is adjusted based on the user’s progress, ensuring accurate tracking.

5. SQLite Database Integration
   - The application uses an SQLite database to store user data securely.
   - All financial transactions, categories, and goal details are saved for easy retrieval and updating.

6. Simulated Responses (For AI-powered insights)
   - Currently, the app simulates AI-generated insights due to external API limitations, ensuring the application is fully functional even without an active API connection.
   - Real-time AI insights will be added once the API quota issue is resolved or another API is integrated.

TECH STACK:
- Python for backend logic and database interaction.
- SQLite as the database for persistent storage of financial data.
- Streamlit for the interactive frontend and UI.
- Plotly for interactive charts and visualizations (e.g., spending trends, goal tracking).
- OpenAI GPT-3 API for generating AI-powered budget insights (Simulated currently due to API quota limits).

USAGE:
1. Adding Categories:
   - Users can add their financial transactions in categories like income,expense,savings.

2. Viewing Insights:
   - The app will provide AI-powered insights (simulated for now) based on the user’s spending patterns.
   - It will offer budget analysis, tips on financial health, and suggestions to achieve financial goals.

3. Savings Goal Tracking:
   - Users can create and track savings goals, such as saving for a vacation, emergency fund, etc.
   - The app provides real-time updates on how close the user is to achieving their goal.

4. Financial Health Score:
   - The app calculates the user’s financial health score based on their income, expenses, and savings.
   - A higher score indicates good financial health, while a lower score suggests areas of improvement.

FUTURE ENHANCEMENTS:
- AI-powered insights integration with OpenAI (once the API quota issue is resolved).
- Extended data visualizations for better financial analysis and forecasting.
- Integration with external financial data sources for automatic transaction importing.
