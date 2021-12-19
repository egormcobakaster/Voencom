import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

cur = conn.cursor()
n = 0
for i in range(200):
    num = random.randint(1, 5)
    voenkomat_id = 1000 + i
    voenchasts = random.choices(range(100), k=num)
    for j in range(num):
        voenchast_id  = 1000 + voenchasts[j]
        cur.execute(
            "INSERT INTO Voen_chast_for_Voenkomats (id, voenkomat_id, voenchast_id) VALUES (%s, %s, %s)",
            (1000 + n, voenkomat_id, voenchast_id,)
        )
        n = n + 1
conn.commit()