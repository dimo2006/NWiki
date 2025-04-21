import sqlite3

def connect():
    return sqlite3.connect('database.db')

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            des TEXT NOT NULL,
            edit_date TEXT NOT NULL,
            edit_by TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_entries():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    conn.close()
    return entries

def add_entry(name, des, edit_date, edit_by, subject):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (name, des, edit_date, edit_by, subject) VALUES (?, ?, ?, ?, ?)', (name, des, edit_date, edit_by, subject))
    conn.commit()
    conn.close()

def get_entry(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries WHERE id = ?', (id,))
    entry = cursor.fetchone()
    conn.close()
    return {'id': entry[0], 'name': entry[1]} if entry else None

def update_entry(id, name, des, edit_date, edit_by, subject):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE entries SET name = ?, des = ?, edit_by = ?, edit_date = ?, subject = ? WHERE id = ?', (name,des, edit_date, edit_by, subject, id))
    conn.commit()
    conn.close()

def delete_entry(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM entries WHERE id = ?', (id,))
    conn.commit()
    conn.close()
