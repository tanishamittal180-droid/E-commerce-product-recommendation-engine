import sqlite3
import os

# -------------------------
# DATABASE PATH
# -------------------------

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "database.db"
)

# -------------------------
# CONNECTION
# -------------------------

def get_connection():
    return sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

# -------------------------
# REGISTER USER
# -------------------------

def register_user(username, email, password):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
        INSERT INTO users(username, email, password)
        VALUES (?, ?, ?)
        """, (username, email, password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

# -------------------------
# LOGIN USER
# -------------------------

def login_user(username, password):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM users
    WHERE username=? AND password=?
    """, (username, password))

    user = cur.fetchone()

    conn.close()

    return user

# -------------------------
# CART
# -------------------------

def add_to_cart(username, product_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO cart(username, product_id)
    VALUES (?, ?)
    """, (username, product_id))

    conn.commit()
    conn.close()

def get_cart(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT product_id
    FROM cart
    WHERE username=?
    """, (username,))

    data = cur.fetchall()

    conn.close()

    return data

# -------------------------
# WISHLIST
# -------------------------

def add_to_wishlist(username, product_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO wishlist(username, product_id)
    VALUES (?, ?)
    """, (username, product_id))

    conn.commit()
    conn.close()

def get_wishlist(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT product_id
    FROM wishlist
    WHERE username=?
    """, (username,))

    data = cur.fetchall()

    conn.close()

    return data

# -------------------------
# ORDERS
# -------------------------

def place_order(username, product_id, price):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO orders(username, product_id, price)
    VALUES (?, ?, ?)
    """, (username, product_id, price))

    conn.commit()
    conn.close()

def get_orders(username):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM orders
    WHERE username=?
    ORDER BY order_date DESC
    """, (username,))

    data = cur.fetchall()

    conn.close()

    return data

# -------------------------
# REVIEWS
# -------------------------

def add_review(username, product_id, rating, review):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO reviews(
        username,
        product_id,
        rating,
        review
    )
    VALUES (?, ?, ?, ?)
    """, (
        username,
        product_id,
        rating,
        review
    ))

    conn.commit()
    conn.close()

def get_reviews(product_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT username, rating, review
    FROM reviews
    WHERE product_id=?
    """, (product_id,))

    data = cur.fetchall()

    conn.close()

    return data

# -------------------------
# INVENTORY
# -------------------------

def add_inventory(product_id, stock):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO inventory(
        product_id,
        stock
    )
    VALUES (?, ?)
    """, (
        product_id,
        stock
    ))

    conn.commit()
    conn.close()

def get_inventory():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM inventory
    """)

    data = cur.fetchall()

    conn.close()

    return data