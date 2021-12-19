import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)
cur = conn.cursor()
for i in range(300):
    date = datetime.date(random.randint(2019,2021), random.randint(1,12), random.randint(1,28))
    cur.execute(
        "INSERT INTO Medical_boards (id, date) VALUES  (%s, %s)",
        (2000 + i, date)
    )

conn.commit()