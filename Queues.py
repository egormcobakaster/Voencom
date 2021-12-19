import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)


cur = conn.cursor()
n = 0
for i in range(1, 4400):
    coin = random.randint(1, 100)
    if coin > 50:
        cabinet_id = i
        cur.execute("SELECT voenkomat_id FROM Cabinets WHERE id = %s", (cabinet_id,))
        voenkomat_id = cur.fetchone()
        cur.execute("SELECT id FROM conscripts WHERE  voenkomat_id = %s",  voenkomat_id)
        mas = []
        for row in cur:
            mas.append(row[0])
        for j in range(1, len(mas)):
            monetka = random.randint(1, 10)
            if monetka > 7:
                day = random.randint(1, 5)
                for k in range(5):
                    monetka = random.randint(1, 10)
                    if monetka > 7:
                        time = datetime.time(12 + k, 0, 0)
                        сonscript_id = mas[(i + j + k) % len(mas)]
                        cur.execute(
                            "INSERT INTO Queues (id, day, time, cabinet_id, сonscript_id) VALUES (%s, %s, %s, %s, %s)",
                            (1000 + n, day, time, cabinet_id, сonscript_id)
                        )
                        n = n + 1

conn.commit()