import psycopg2

conn = psycopg2.connect(database='db_udacity', user='postgres', password="*")
cursor = conn.cursor()

# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS todos")

cursor.execute("""
    CREATE TABLE todos (id serial PRIMARY KEY, 
    description TEXT NOT NULL)
""")

cursor.execute("INSERT INTO todos (description) VALUES ('Wash clothes');")

conn.commit()

cursor.close()
conn.close()
