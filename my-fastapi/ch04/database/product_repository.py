from ch04.database import DBConnect
from ch04.model.product import Product

db = DBConnect()
cur = db.get_cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL,
                    stock INTEGER NOT NULL,
                    description TEXT
               )""")

def insert(product: Product) -> bool:
    cur.execute("""
        insert into products (name, price, stock, description) values (:name, :price, :stock, :description)
    """, product.model_dump())
    db.commit()
    return True