import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return None

def create_tables(conn):
    """Create products and orders tables"""
    try:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                category TEXT,
                price REAL NOT NULL,
                stock_quantity INTEGER NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id)
            );
        ''')
        conn.commit()
        print("Tables 'products' and 'orders' created successfully.")
    except Error as e:
        print(e)

def insert_product(conn, product):
    """Insert a new product into the products table"""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (product_name, category, price, stock_quantity) VALUES (?, ?, ?, ?)", product)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def insert_order(conn, order):
    """Insert a new order into the orders table"""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (product_id, order_date, quantity, total_price) VALUES (?, ?, ?, ?)", order)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None

def update_row(conn, table, row_id, updates):
    """Update a row in the specified table"""
    try:
        cursor = conn.cursor()
        set_clause = ", ".join([f"{column} = ?" for column in updates.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        values = list(updates.values()) + [row_id]
        cursor.execute(sql, values)
        conn.commit()
        print(f"Wiersz z id {row_id} w tabeli {table} został zaktualizowany.")
    except Error as e:
        print(e)

def select_all(conn, table):
    """Select all rows from the specified table"""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        print(f"Zawartość tabeli {table}:")
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def select_where(conn, table, column, operator, value):
    """Select rows from the table where a condition is met"""
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table} WHERE {column} {operator} ?"
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        print(f"Zawartość tabeli {table}, gdzie {column} {operator} {value}:")
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def delete_where(conn, table, **kwargs):
    """Delete rows from table where conditions are met"""
    try:
        qs = []
        values = tuple()
        for k, v in kwargs.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        sql = f'DELETE FROM {table} WHERE {q}'
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print(f"Usunięto wiersze z tabeli {table}, gdzie: {kwargs}")
    except Error as e:
        print(e)

def delete_all(conn, table):
    """Delete all rows from a table"""
    try:
        sql = f'DELETE FROM {table}'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print(f"Wszystkie wiersze z tabeli {table} zostały usunięte.")
    except Error as e:
        print(e)

def insert_sample_data(conn):
    """Insert sample data using the insert_product and insert_order functions"""

    product1 = ('Telefon', 'Elektronika', 999.99, 10)
    product2 = ('Laptop', 'Elektronika', 1500.00, 5)

    product1_id = insert_product(conn, product1)
    print(f"Ostatni wstawiony product_id dla Produkt 1: {product1_id}")

    product2_id = insert_product(conn, product2)
    print(f"Ostatni wstawiony product_id dla Produkt 2: {product2_id}")

    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    order1 = (product1_id, order_date, 2, 1999.98)  
    order2 = (product2_id, order_date, 1, 1500.00)   

    order1_id = insert_order(conn, order1)
    print(f"Ostatni wstawiony order_id dla Order 1: {order1_id}")

    order2_id = insert_order(conn, order2)
    print(f"Ostatni wstawiony order_id dla Order 2: {order2_id}")

if __name__ == '__main__':
    conn = create_connection(r"mydatabase.db")
    if conn:
        create_tables(conn)
        insert_sample_data(conn)

         # Test funkcji select_where dla tabeli products
        # Dodaje przykładowe dane do tabeli products
        insert_product(conn, ('Testowy Produkt', 'Elektronika', 299.99, 20))
        print("Test funkcji select_where dla tabeli products (kategoria = 'Elektronika'):")
        select_where(conn, "products", "category", "=", "Elektronika")
        product_id = 1  # Przykładowe ID, załóżmy, że ten produkt istnieje w bazie
        insert_order(conn, (product_id, '2024-10-28 10:00:00', 3, 899.97))

        # Używam funkcji select_where, aby znaleźć zamówienie z quantity większym niż 1
        print("Test funkcji select_where dla tabeli orders (quantity > 1):")
        select_where(conn, "orders", "quantity", ">", 1)

        conn.close()
        
