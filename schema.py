import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# -----------------------------
# USERS TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")

# -----------------------------
# WISHLIST TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS wishlist(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    product_id TEXT
)
""")

# -----------------------------
# CART TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    product_id TEXT,
    quantity INTEGER DEFAULT 1
)
""")

# -----------------------------
# ORDERS TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    product_id TEXT,
    price REAL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# -----------------------------
# REVIEWS TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    product_id TEXT,
    rating INTEGER,
    review TEXT
)
""")

# -----------------------------
# INVENTORY TABLE
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT UNIQUE,
    stock INTEGER
)
""")

# -----------------------------
# SAVE CHANGES
# -----------------------------

conn.commit()
conn.close()

print("✅ Database Ready Successfully")