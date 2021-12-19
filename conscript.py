import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)

cities = "Москва Санкт-Петербург Новосибирск Екатеринбург Казань Нижний Новгород Челябинск"
cities = cities.split()
streets = "Центральная Молодежная Школьная Лесная  Садовая  Советская Новая  Набережная"
streets = streets.split()
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
cur = conn.cursor()
n = 0
for i in range(200):
    voenkomat_id = 1000 + i
    for j in range(random.randint(3, 10)):
        age = random.randint(16,28)
        name = random.choice(names)
        surname = random.choice(surnames)
        patronymic = random.choice(patronymics)
        city = random.choice(cities)
        street = random.choice(streets)
        house_num = random.randint(1,200)
        flat_num = random.randint(1,500)
        category = flat_num < 400
        subpoena = house_num > 30

        medical_boards_id = 2000 + i
        cur.execute(
            "INSERT INTO Conscripts (id, age, name, surname, patronymic, "
            "city, street, house_num, flat_num, category, subpoena, voenkomat_id, medical_boards_id)"
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (n, age, name, surname, patronymic, city, street, house_num, flat_num, category, subpoena, voenkomat_id, medical_boards_id)
        )
        n = n +1

conn.commit()