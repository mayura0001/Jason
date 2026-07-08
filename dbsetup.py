"""

---Data-Types---
NULL - Represents a null value
INTEGER - Represents an integer value
REAL - Represents a floating-point number
TEXT - Represents a text string
BLOP - Represents a binary large object (ex. images, audio, etc.)

"""


import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
c = conn.cursor()

