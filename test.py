# import sqlite3

# # Connect to your SQLite database
# conn = sqlite3.connect('testDB.db')
# cursor = conn.cursor()

# # Add a new column to the 'todos' table
# cursor.execute('ALTER TABLE todos ADD COLUMN username TEXT;')

# # Commit changes and close the connection
# conn.commit()
# conn.close()

# print("Column added successfully.")




import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('testDB.db')
cursor = conn.cursor()

# Step 1: Create the new table (without the 'user_id' column)
cursor.execute('''
    CREATE TABLE todos_new (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        category TEXT,
        name TEXT,
        text TEXT
    );
''')

# Step 2: Copy data from the old table to the new table (excluding 'user_id')
cursor.execute('''
    INSERT INTO todos_new (id, username, category, name, text)
    SELECT id, username, category, name, text FROM todos;
''')

# Step 3: Drop the old table
cursor.execute('DROP TABLE todos;')

# Step 4: Rename the new table to 'todos'
cursor.execute('ALTER TABLE todos_new RENAME TO todos;')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Column 'user_id' removed and table updated successfully.")









# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('testDB.db')
# cursor = conn.cursor()

# # Add the 'id' column with the AUTOINCREMENT option if it doesn't exist
# cursor.execute('PRAGMA foreign_keys=off;')  # Temporarily disable foreign key checks
# cursor.execute('ALTER TABLE users ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT;')
# cursor.execute('ALTER TABLE users ADD COLUMN username TEXT UNIQUE;')
# cursor.execute('PRAGMA foreign_keys=on;')  # Re-enable foreign key checks

# # Commit changes and close the connection
# conn.commit()
# conn.close()

# print("Columns added successfully.")
