import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

conscripts = random.choices(range(1000, 1500), k=200)
cur = conn.cursor()
for i in range(200):
    voenchast_id = random.randint(1000, 1099)
    cur.execute("SELECT voenkomat_id FROM Voen_chast_for_Voenkomats WHERE voenchast_id = %s", (voenchast_id,))
    mas = []
    for row in cur:
        mas.append(row[0])
    voenkomat_id = random.choice(mas)
    start = datetime.date(random.randint(2019,2021), random.randint(1,12), random.randint(1,28))
    ending = datetime.date(start.year + 1, start.month, start.day)
    cur.execute("SELECT id FROM conscripts WHERE voenkomat_id = %s", (voenkomat_id,))
    mas = []
    for row in cur:
        mas.append(row[0])
    сonscript_id = random.choice(mas)
    cur.execute(
        "INSERT INTO Military_orders (id, ending, Start, сonscript_id, voenchast_id, voenkomat_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (1000 + i, ending, start, сonscript_id, voenchast_id, voenkomat_id)
    )

conn.commit()