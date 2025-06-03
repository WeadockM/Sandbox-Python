# db.py
import sqlite3

# Connect to the SQLite database
dbConnection = sqlite3.connect('./database/users.db')
dbCursor = dbConnection.cursor()

def create_table():
    """Create the users table if it doesn't exist"""
    dbCursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL)''')
    
    # Add a test user if the table is empty
    dbCursor.execute('SELECT id FROM users WHERE id = 1')
    if not dbCursor.fetchone():
        dbCursor.execute("INSERT OR REPLACE INTO users (id, username, email, password) VALUES (?, ?, ?, ?)", 
                         (1, 'admin', 'admin@aol.com', 'admin'))
        dbConnection.commit()

def list_all_users():
    """Return all users from the database"""
    res = dbCursor.execute("SELECT id, username, email FROM users")
    return res.fetchall()

def get_user_by_credentials(username, password):
    dbCursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return dbCursor.fetchone()

def update_password(user_id, new_password):
    dbCursor.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
    dbConnection.commit()

def update_user(user_id, new_username, new_email):
    dbCursor.execute("UPDATE users SET username = ?, email = ? WHERE id = ?", (new_username, new_email, user_id))
    dbConnection.commit()

def insert_user(username, password, email):
    dbCursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
    dbConnection.commit()

def get_connection():
    return dbConnection

def get_cursor():
    return dbCursor
