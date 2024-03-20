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
    conn.close()

if __name__ == "__main__":
    create_tables()
