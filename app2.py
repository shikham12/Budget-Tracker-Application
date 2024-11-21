import sqlite3
import streamlit as st 
import pandas as pd 
import openai
import os
import numpy as np
import plotly.express as px
from db import (
    create_connection,
    create_user_table,
    create_user,
    authenticate_user,
    create_categories_table,
    create_savings_goal_table,
    get_goal_data
)
from financial_health_score import FinancialHealthScore
from savings_goal_tracker import SavingsGoalTracker
from get_budget_insight import simulate_insight

openai.api_key="api_key"
st.set_page_config(page_title='Budget Tracker')

st.title(':red[Budget Tracker]')

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False 
if 'user_id' not in st.session_state:
    st.session_state.user_id = None 

signup_tab, login_tab, category_tab, savings_tab, ai_tab= st.tabs(['SignUp', 'Login', 'Add and Manage Categories', 'Savings Tracker and Financial Health Score','AI-Assistant'])

with signup_tab:
    username = st.text_input('Choose your user id', key='signupusernamekey')
    password = st.text_input('Choose your Password', type='password', key='signuppasswordkey')
    signup_button = st.button('Create your account', key='signupbuttonkey')

    if signup_button:
        if username and password:
            try:
                create_user(username, password)
                st.success('Account created successfully. Go to the login page')
            except sqlite3.IntegrityError:
                st.error('Username already exists.')
        else:
            st.warning('Please provide username and password')

with login_tab:
    username = st.text_input('Enter your user id', key='loginusernamekey')
    password = st.text_input('Enter your Password', type='password', key='loginpasswordkey')
    login_button = st.button('Login', key='loginbuttonkey')

    if login_button:
        if username and password:
            user = authenticate_user(username, password)  # Should return a user tuple
            if user:
                st.session_state.logged_in = True
                st.session_state.user_id = user[0]  # Assuming user[0] is the user ID
                st.success(f'Welcome {username}, let us track your budget')



            else:
                st.error('Invalid Username or password')
        else:
            st.warning('Please enter username and password')

if st.session_state.logged_in:
    with category_tab:
        def add_category(category_name, category_type):
            conn = create_connection()
            c = conn.cursor()
            c.execute('INSERT INTO categories_table (user_id, category_name, category_type) VALUES (?, ?, ?)',
                      (st.session_state.user_id, category_name, category_type))
            conn.commit()
            conn.close()
        
        def display_categories():
            conn = create_connection()
            c = conn.cursor()
            c.execute('SELECT category_name, category_type FROM categories_table WHERE user_id = ?',
                      (st.session_state.user_id,))
            categories = c.fetchall()
            conn.close()

            if categories:
                df = pd.DataFrame(categories, columns=['Category Name', 'Category Type'])
                st.subheader('Your Category Table')
                st.dataframe(df) 
                data = df['Category Type'].value_counts().reset_index()
                st.subheader('Analysis')
                st.dataframe(data)
                st.subheader('Visualization')
                fig = px.bar(data_frame=data, x='Category Type', y='count', text='count')
                st.plotly_chart(fig)
            else:
                st.write(':red[No Categories Found. Please add categories]')
        
        st.subheader('Add and manage categories')
        category_name = st.text_input('Subcategory', key='categoryname')
        category_type = st.selectbox('Category Type', options=['expense', 'income', 'savings'])
        category_button = st.button('Add Category', key='categorybutton')

        if category_button:
            if category_name:
                add_category(category_name, category_type)
                st.success("Category added successfully")
            else:
                st.warning("Please enter category name")

        display_categories()


    with savings_tab:
        st.subheader("Savings Tracker, Financial Health Score")

        # Inputs for user to enter their financial data
        income = st.number_input("Enter your monthly income:", min_value=0.0)
        expenses = st.number_input("Enter your monthly expenses:", min_value=0.0)
        savings = st.number_input("Enter your current savings:", min_value=0.0,step=10.0)
        goal_amount = st.number_input("Savings Goal Amount :", min_value=0.0, step=100.0)
        months_to_goal = st.number_input("Months to Reach Goal:", min_value=1, step=1)

    # Call the savings_goal_tracker function
        progress, remaining_amount = SavingsGoalTracker(goal_amount, savings, months_to_goal)

    # Display the savings goal tracker
        st.header("Savings Goal Tracker:")
        st.write(f"Goal Amount: {goal_amount:.2f}")
        st.write(f"Total Savings by Goal Date: {savings * months_to_goal:.2f}")
        st.write(f"Progress: {progress:.2f}%")
        st.write(f"Remaining Amount: {remaining_amount:.2f}")
        st.progress(progress / 100)

    # Add a success message if the user has reached their goal
        if progress >= 100:
            st.success("Congratulations! You've reached your savings goal!")
        # Call the savings_goal_tracker function
            progress, remaining_amount = SavingsGoalTracker(goal_amount)

        # Call the calculate_financial_health_score function
        score = FinancialHealthScore(income, expenses, savings)

    # Display the financial health score
        st.header("Your Financial Health Score:")
        st.write(f"Score: {score:.2f}/100")

    # Provide feedback based on the score
        if score >= 80:
            st.success("Excellent financial health! Keep up the great work!")
        elif score >= 50:
            st.warning("Good financial health, but there's room for improvement.")
        else:
            st.error("Your financial health needs attention. Consider reviewing your expenses and savings.")

with ai_tab:
    st.header("AI-Powered Budget Insight Assistant")
    user_query = st.text_input("Ask for financial advice:", placeholder="How can I save more?")
    #insight = get_budget_insight(user_data, user_query)  # Function defined below
    insight = simulate_insight(user_query, query="Give me budget insights.")
    st.write("### Insight:")
    st.write(insight)

