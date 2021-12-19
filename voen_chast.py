import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

cities = "Москва Санкт-Петербург Новосибирск Екатеринбург Казань Нижний Новгород Челябинск"
cities = cities.split()
peh = "Пехота Кавалерия Артиллерия Танковые_войска Войска_противовоздушной_обороны Аэромобильные_войска"
vms = "Надводные_силы Морская_пехота Подводные_силы Морская_авиация Береговые ракетно-артиллерийские_войска"
typee = peh + ' ' + vms
typee = typee.split()
cur = conn.cursor()
for i in range(100):
    city = random.choice(cities)
    voisk = random.choice(typee)
    count = random.randint(200, 1000)
    cur.execute(
        "INSERT INTO voen_chast (id, type_of_army, city,  soldier_count) VALUES (%s, %s, %s, %s)",
        (1000 + i, voisk, city, count)
    )

conn.commit()