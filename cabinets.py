import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

cur = conn.cursor()
n = 1
for i in range(200):
    voenkomat_id = 1000 + i
    for j in range(20):

        num = 110 + j
        type = 'медицинский'
        cur.execute(
            "INSERT INTO Cabinets (id,type, num, voenkomat_id) VALUES (%s, %s, %s, %s)",
            (n, type, num, voenkomat_id)
        )
        n = n + 1
    cur.execute(
            "INSERT INTO Cabinets (id,type, num, voenkomat_id) VALUES (%s, %s, %s, %s)",
            (n, 'регистратура', 1, voenkomat_id)
    )
    n = n + 1
    cur.execute(
            "INSERT INTO Cabinets (id,type, num, voenkomat_id) VALUES (%s, %s, %s, %s)",
            (n, 'тестирование', 200, voenkomat_id)
    )
    n = n + 1
conn.commit()