import tkinter as tk
from tkinter import messagebox

import sqlite3

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
create_tables()
def login():
    usernamein = username_entry.get()
    passwordin = password_entry.get()

    print(usernamein)
    print(passwordin)
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('SELECT username FROM users WHERE username == ?', (usernamein,)) 

    username_result = c.fetchone()
    print(username_result)

# Execute the query to retrieve the hashed password for the given username
    c.execute('SELECT passwordhash FROM users WHERE passwordhash == ?', (passwordin,))
    password_result = c.fetchone()
    print(password_result)

# Check if the username and password match
    if username_result is not None and password_result is not None and "('" + passwordin + "',)" == password_result:
        messagebox.showinfo("Login Successful", "Welcome, " + usernamein + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    # Check if username and password are correct
    #if usernamein == c.execute('Select username from users where username== ?',("usernamein")) and passwordin == c.execute('Select passwordhash from users where passwordhash== ?',(passwordin)):
     #   messagebox.showinfo("Login Successful", "Welcome, " + usernamein + "!")
    #else:
     #   messagebox.showerror("Login Failed", "Invalid username or password")

def create_account_window():
    create_window = tk.Toplevel(root)
    create_window.title("Create Account")

    tk.Label(create_window, text="Enter new username:").pack()
    new_username_entry = tk.Entry(create_window)
    new_username_entry.pack()

    tk.Label(create_window, text="Enter new password:").pack()
    new_password_entry = tk.Entry(create_window, show="*")
    new_password_entry.pack()

    def create_account():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
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
        create_window.destroy()

    tk.Button(create_window, text="Create", command=create_account).pack()

# Create the main window
root = tk.Tk()
root.title("Login Screen")

# Create labels and entries for username and password
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Create create account button
create_account_button = tk.Button(root, text="Create Account", command=create_account_window)
create_account_button.pack()

# Run the main event loop
root.mainloop()