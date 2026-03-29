# I am learning how to use SQL with Python to stay organized during the application periods.
# This is much better than a simple paper list as it helps me prctice the skills I am learning.

import sqlite3

# Step 1 is to create or connect to the database file
db = sqlite3.connect("my_applications.db")
cursor = db.cursor()

# Step 2 is about creating a Table (The Structure)
# I am defining what information I want to save for each university.
print("Setting up the Database Structure")

cursor.execute("""
CREATE TABLE IF NOT EXISTS university_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uni_name TEXT,
    country TEXT,
    major TEXT,
    language_req TEXT,
    status TEXT
)
""")

# Step 3 is to show the list of some universities I would like to apply to.
# I am focusing on Business and Data Science in Europe.

my_targets = [
    ('Maastricht University', 'Netherlands', 'Data Science and AI', 'English (IELTS 8.0)', 'Interested'),
    ('University of Bologna', 'Italy', 'Management and Economics', 'English/Italian', 'Researching'),
    ('IE University', 'Spain', 'Data and Business Analytics', 'English/Spanish', 'Will look more into it'),
    ('Sapienza University', 'Italy', 'Applied Data Science', 'English', 'Planning'),
 
]

# Step 4 is adding the data to the SQL table

print("Adding Universities to the System")

for uni in my_targets:
    cursor.execute("""
    INSERT INTO university_list (uni_name, country, major, language_req, status) 
    VALUES (?, ?, ?, ?, ?)
    """, uni)

# Saving the changes
db.commit()

# Step 5: Reading the data back to make sure everything is neat and tidy.
# I want to see my list in a clean, professional table format, that is why.
print("\n--- MY CURRENT UNIVERSITY TARGET LIST ---")
print("-" * 50)

cursor.execute("SELECT * FROM university_list")
all_unis = cursor.fetchall()

for row in all_unis:
    # row[0] is the ID, row[1] is name, etc.
    print(f"ID: {row[0]} | {row[1]} ({row[2]})")
    print(f"   Major: {row[3]}")
    print(f"   Requirement: {row[4]}")
    print(f"   Current Status: {row[5]}")
    print("-" * 50)

# Closing the connection to keep it safe
db.close()
print("\nDatabase scan complete")


# I used 'AUTOINCREMENT' for IDs so the database counts the unis itself.
# Next time, I want to learn how to UPDATE the status (e.g., from 'Planning' to 'Applied') so I can make it more professional.
