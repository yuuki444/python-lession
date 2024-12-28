import sqlite3

conn = sqlite3.connect('db.sl3')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS test')
cursor.execute('''CREATE TABLE IF NOT EXISTS test(
    first_name TEXT, 
    last_name TEXT, 
    money INT)''')


cursor.execute('INSERT INTO test VALUES ("John", "Doe", 100)')
cursor.execute('INSERT INTO test VALUES ("Jane", "Doe", 200)')
cursor.execute('INSERT INTO test VALUES ("Jim", "Doe", 300)')

cursor.execute("UPDATE test SET money = money - 100 WHERE first_name = 'John'") 
cursor.execute("UPDATE test SET money = money + 100 WHERE first_name = 'Jim'")
cursor.execute("SELECT first_name, money FROM test WHERE first_name IN ('John', 'Jim')")
rows = cursor.fetchall()


for row in rows:
    print(f"{row[0]} now has {row[1]} money.")
conn.commit()
conn.close()
