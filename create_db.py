import sqlite3

# Connection to DB
conn = sqlite3.connect('swipeat.db')

# Cursor
c = conn.cursor()

# Create swipeat_accounts table
c.execute("CREATE TABLE swipeat_accounts (username text, password text)")
conn.commit()

