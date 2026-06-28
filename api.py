from fastapi import FastAPI
import sqlite3

path_db = 'data/sales.db'
app = FastAPI()

def get_connection():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    return conn, cursor

def row_to_dict(cursor):
    columns = [col[0] for col in cursor.description]
    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return data

def get_sales():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM sales")
    data = row_to_dict(cursor)
    conn.close()
    return data

def get_sale_by_id(id: int):
    conn, cursor = get_connection()
    cursor.execute('SELECT * FROM sales WHERE order_id = ?', (id,))
    data = row_to_dict(cursor)
    conn.close()
    return data

def get_sale_by_city(city: str):
    conn, cursor = get_connection()
    cursor.execute('SELECT * FROM sales WHERE city = ?', (city,))
    data = row_to_dict(cursor)
    conn.close()
    return data

def get_sale_by_payment_method(payment_method: str):
    conn, cursor = get_connection()
    cursor.execute('SELECT * FROM sales WHERE payment_method = ?', (payment_method,))
    data = row_to_dict(cursor)
    conn.close()
    return data

def get_rejected():
    conn, cursor = get_connection()
    cursor.execute('SELECT * FROM rejected_sales')
    data = row_to_dict(cursor)
    return data

def get_summary():
    conn, cursor = get_connection()
    cursor.execute('SELECT(SELECT COUNT(*) FROM sales)+(SELECT COUNT(*) FROM rejected_sales) AS total_records,(SELECT SUM(unit_price) FROM sales) AS total_sum;')
    data = row_to_dict(cursor)
    conn.close()
    return data


@app.get('/sales')
def list_sales():
    sales = get_sales()
    return sales

@app.get('/sales/{order_id}')
def list_get_sales_id(order_id: int):
    data = get_sale_by_id(order_id)
    return data

@app.get('/sales/city/{city}')
def list_get_sales_city(city: str):
    data = get_sale_by_city(city)
    return data

@app.get('/sales/payment_method/{payment_method}')
def list_get_sales_payment_method(payment_method: str):
    data = get_sale_by_payment_method(payment_method)
    return data

@app.get('/rejected')
def list_rejected():
    data = get_rejected()
    return data

@app.get('/summary')
def summary():
    data = get_summary()
    return data
