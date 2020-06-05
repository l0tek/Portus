import sqlite3

conn = sqlite3.connect('bay.db')
print("Opened database successfully")

conn.execute('CREATE TABLE bookmarks (url TEXT, title TEXT, cat TEXT)')
print("Table created successfully")
conn.close()