import sqlite3
import tkinter as tk
from tkinter import messagebox

def get_db_connection(database_name='huskyvault.db'):
    return sqlite3.connect(database_name)

def create_tables():
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (userid INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, passwordhash TEXT, salt TEXT, createdat TEXT, updatedat TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS securepasswords
                 (passwordid INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER, title TEXT, emailorusername TEXT, encryptedpassword TEXT, siteurl TEXT, description TEXT, createdat TEXT, updatedat TEXT,
                 FOREIGN KEY(userid) REFERENCES users(userid))''')
    c.execute('''CREATE TABLE IF NOT EXISTS securenotes
                 (noteid INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER, title TEXT, notetext TEXT, createdat TEXT, updatedat TEXT,
                 FOREIGN KEY(userid) REFERENCES users(userid))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()


def login(usernamein, passwordin):
    print(usernamein)
    print(passwordin)
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('SELECT username FROM users WHERE username == ?', (usernamein,))

    username_result = c.fetchone()

# Execute the query to retrieve the hashed password for the given username
    c.execute('SELECT passwordhash FROM users WHERE passwordhash == ?', (passwordin,))
    password_result = c.fetchone()

# Check if the username and password match
    if username_result is None or password_result is None:
        messagebox.showerror("Login Failed", "Invalid username or password")
    elif username_result[0] is not None and password_result is not None and passwordin == password_result[0]:
        messagebox.showinfo("Login Successful", "Welcome, " + usernamein + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def create_account(new_username, new_password):
    # Here you would typically save the new username and password
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO users (username, passwordhash, salt, createdat, updatedat) VALUES (?, ?, ?, ?, ?)',(new_username, new_password, "text", "text", "test"))
    conn.commit()

    c.execute('select * from users')
    rows = c.fetchall()
    for row in rows:
        print(row)
    messagebox.showinfo("Account Created", "You can now use your new account to login")

