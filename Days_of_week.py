import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)


days = range(1,6)
k = 1
cur = conn.cursor()
for i in range(1, 4401):
    cabinet_id = i
    n = random.randint(1, 5)
    sample = random.sample(days, k=n)
    print(sample)
    for day in sample:

        start = datetime.time(random.randint(8,11), 0, 0, 0)
        end = datetime.time(random.randint(16, 19), 0, 0, 0)
        cur.execute(
            "INSERT INTO Days_of_week (id, dayofweek, _start, _end, cabinet_id) VALUES (%s, %s, %s, %s, %s)",
            (1000 + k, day, start, end, cabinet_id)
        )
        k = k + 1
conn.commit()