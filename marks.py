import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS students (roll TEXT, name TEXT, maths INT, science INT)')

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    maths = int(input("Maths: "))
    science = int(input("Science: "))
    c.execute("INSERT INTO students VALUES (?,?,?,?)", (roll, name, maths, science))
    conn.commit()
    print("Saved!")

def show_all():
    for row in c.execute("SELECT * FROM students"):
        print(f"{row[0]} | {row[1]} | Total: {row[2]+row[3]}")

while True:
    print("\n1.Add 2.Show 3.Exit")
    ch = input("Choice: ")
    if ch == '1': add_student()
    elif ch == '2': show_all()
    else: break

conn.close()
