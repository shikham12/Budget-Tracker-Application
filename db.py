import sqlite3

import pandas as pd


# Create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('bud.db')
    return conn 

# Creates a user table
def create_user_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_table (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Create a new user in the database
def create_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_table (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Authenticate user
def authenticate_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM user_table WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Create categories table
def create_categories_table():
    conn = create_connection()    
    c = conn.cursor()    
    c.execute('''CREATE TABLE IF NOT EXISTS categories_table (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,  
                user_id INTEGER,
                amount REAL,
                description TEXT,
                date TEXT,
                category_name TEXT NOT NULL,             
                category_type TEXT NOT NULL CHECK(category_type IN ('expense', 'income', 'savings')),
                FOREIGN KEY (user_id) REFERENCES user_table(id) )    
              ''')   
    conn.commit()    
    conn.close()

# Create savings goals table
def create_savings_goal_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            goal_amount REAL,
            current_savings REAL,
            FOREIGN KEY (user_id) REFERENCES user_table(id)
        )''')
    conn.commit()
    conn.close()

# Add a new savings goal
def add_savings_goal(user_id, goal_amount):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO savings_goals (user_id, goal_amount, current_savings) VALUES (?, ?, ?)', 
              (user_id, goal_amount, 0))  # Initialize current savings to 0
    conn.commit()
    conn.close()

# Update current savings for a goal
def update_current_savings(goal_id, amount):
    conn = create_connection()
    c = conn.cursor()
    c.execute('UPDATE savings_goals SET current_savings = current_savings + ? WHERE id = ?', 
              (amount, goal_id))
    conn.commit()
    conn.close()

# Retrieve savings goals for a user
def get_savings_goals(user_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM savings_goals WHERE user_id = ?', (user_id,))
    goals = c.fetchall()
    conn.close()
    return goals

# Retrieve goal data as a pandas DataFrame
def get_goal_data(user_id):
    conn = create_connection()
    query = '''
        SELECT goal_amount, current_savings
        FROM savings_goals
        WHERE user_id = ?
    '''
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()
    return df




    



# Create tables
create_connection()
create_user_table()
create_categories_table()
create_savings_goal_table()
#create_user_segments_table(conn)
