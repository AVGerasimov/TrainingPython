import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    us = 'username'+str(i)
    em = 'example'+str(i)+"@gmail.com"
    ag = 10*i
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (us, em, ag, 1000))

for i in range(1, 11):
    if i%2 !=0:
        usn = 'username'+str(i)
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, usn))


for i in range(1, 11):
    if i%3 ==1:
        usn = 'username'+str(i)
        cursor.execute("DELETE FROM Users  WHERE username = ?",  (usn,))


cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
s = 0
for user in users:
    s+=1
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
    print(f'counter= {s}')


#cursor.execute("SELECT MIN(age) FROM Users")
#total3 = cursor.fetchone()[0]
#print(f"function MIN age = {total3}")

cursor.execute('''DELETE FROM Users WHERE id == 6''') # удаление всех данных таблицы Users c id == 6

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(f"Общее количество пользователей = {total1}")

cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(f"sum balance = {total2}")

cursor.execute("SELECT AVG(balance) FROM Users")
total3 = cursor.fetchone()[0]
print(f"Average balance = {total3}")


#cursor.execute('''DELETE FROM Users''') # удаление всех данных таблицы Users

connection.commit()
connection.close()

