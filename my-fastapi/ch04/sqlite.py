import sqlite3

conn = sqlite3.connect("./test.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                stock INTEGER NOT NULL,
                description TEXT
)""")

# 데이터 집어쳐넣기 (like 깜빵에 죄수 넣기)

cur.execute("""INSERT INTO products (name, price, stock, description) VALUES(?,?,?,?)""",
            ("notebook", 1000000, 10, "맥북임"))

name = "pad"
cur.execute(f"""INSERT INTO products (name, price, stock, description) VALUES('{name}',20000,2,"qwe")""")

conn.commit()

# 데이터 수정
param = {"price" : 500000, "name" : "phone"}
cur.execute("UPDATE products SET price=:price, name=:name WHERE id=1", param)
conn.commit()

# 데이터 삭제
notebook = {"name" : "notebook"}
cur.execute("delete from products where name=:name", notebook)
conn.commit()

# 데이터 조회
cur.execute("SELECT * FROM products")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()