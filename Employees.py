import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

names = "Корней,Леонардо,Рианна,Гарри,Север,Северина,Весна,Океана,Марс,Люций,Люцифер,Оливье"
names = names.split(",")
surnames = ['Смирнов',
'Иванов',
'Кузнецов',
'Соколов',
'Попов',
'Лебедев',
'Козлов',
'Новиков',
'Морозов',
'Петров',
'Волков',
'Соловьёв',
'Васильев',
'Зайцев',
'Павлов',
'Семёнов',
'Виноградов',
'Богданов',
'Воробьёв',
'Фёдоров']
patronymics = [
'Александрович',
'Игоревич',
'Сергеевич',
'Геннадьевич',
'Дмитриевич',
'Никитич',
'Ильич',
]
doctors =[
'Терапевт',
'Хирург',
'Офтальмолог',
'Уролог',
]
voen_post=[
    'генерал',
    'секретарь'
]
cur = conn.cursor()
for i in range(1, 4401):
    cur.execute("SELECT type FROM Cabinets WHERE id = %s", (i,))
    type = cur.fetchone()
    cur.execute("SELECT voenkomat_id FROM Cabinets WHERE id = %s", (i,))
    voenkomat_id = cur.fetchone()
    type = type[0]
    voenkomat_id = voenkomat_id[0]
    if type == 'медицинский':
        post = random.choice(doctors)
        typename = 'врач'
    elif type == 'регистратура':
        post = 'секретарь'
        typename = 'не врач'
    else:
        post = 'генерал'
        typename = 'не врач'
    name = random.choice(names)
    surname = random.choice(surnames)
    patronymic = random.choice(patronymics)
    beg = datetime.time(random.randint(8,11), random.choice([0, 20, 40]), 0, 0)
    end = datetime.time(random.randint(16, 19), random.choice([0, 20, 40]), 0, 0)
    cur.execute(
        "INSERT INTO Employees (id, type, name, surname, patronymic, post, cabinet_id, voenkomat_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (1000 + i, typename, name, surname, patronymic, post, i, voenkomat_id)
    )

conn.commit()