import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

cities = "Москва Санкт-Петербург Новосибирск Екатеринбург Казань Нижний Новгород Челябинск"
cities = cities.split()
streets = "Центральная Молодежная Школьная Лесная  Садовая  Советская Новая  Набережная"
streets = streets.split()
cur = conn.cursor()
for i in range(200):
    num = i
    city = random.choice(cities)
    street = random.choice(streets)
    beg = datetime.time(random.randint(8,11), random.choice([0, 20, 40]), 0, 0)
    end = datetime.time(random.randint(16, 19), random.choice([0, 20, 40]), 0, 0)
    cur.execute(
        "INSERT INTO voenkomats (id, city, street, house_num, opening, closure) VALUES (%s, %s, %s, %s, %s, %s)",
        (1000 + i, city, street, i*2 % 200, beg, end)
    )

conn.commit()