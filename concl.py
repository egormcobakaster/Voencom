import psycopg2
import random
import datetime

conn = psycopg2.connect(database="postgres", user="postgres",
    password="Egorip18", host="localhost", port=5432)
cur = conn.cursor()
helth = ['здоров', 'не здоров']
n = 0
for i in range(1286):
    coin = random.randint(1, 100)
    if coin > 50:
        cur.execute("SELECT voenkomat_id FROM Conscripts WHERE id = %s", (i,))
        voenkomat_id = cur.fetchone()
        voenkomat_id = voenkomat_id[0]
        print(voenkomat_id)
        cur.execute("SELECT medical_boards_id FROM conscripts WHERE id = %s", (i,))
        med_bord = cur.fetchone()
        cur.execute("SELECT id FROM employees WHERE voenkomat_id = %s AND type = 'врач'", (voenkomat_id, ))
        medical_boards_id = med_bord[0]
        employees = cur.fetchone()
        for row in employees:
            print(row)
            employees_id =  row
            conclusion = random.choice(helth)
            сonscript_id = i
            cur.execute(
                "INSERT INTO Сonclusions_of_doctors (id, Сonclusion, сonscript_id, employees_id, medical_boards_id) VALUES (%s, %s, %s, %s, %s)",
                (n, conclusion, сonscript_id, employees_id, medical_boards_id)
            )
            n = n +1


conn.commit()