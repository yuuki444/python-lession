import sqlite3
import random
import os

def connect_db():
    conn = sqlite3.connect('bank.db')
    return conn


def clear_db():
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute('DROP TABLE IF EXISTS users')
    conn.commit()
    conn.close()
    print("Таблица очищена.")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL NOT NULL DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()


def create_account(name):
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute('''
    SELECT * FROM users WHERE name = ?
    ''', (name,))

    if cursor.fetchone():
        print(f"Аккаунт с именем {name} уже существует.")
    else:
        cursor.execute('''
        INSERT INTO users (name, balance) VALUES (?, ?)
        ''', (name, 0.0)) 
        conn.commit()
        print(f"Аккаунт для {name} успешно создан.")

    conn.close()


def work(name):
    conn = connect_db()
    cursor = conn.cursor()


    amount = random.randint(200000, 300000)
    cursor.execute('''
    UPDATE users SET balance = balance + ? WHERE name = ?
    ''', (amount, name))

    conn.commit()
    conn.close()
    print(f"Рустем, вы заработали {amount} тенге!")

def check_balance(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT balance FROM users WHERE name = ?
    ''', (name,))
    result = cursor.fetchone()

    if result:
        print(f"Ваш текущий баланс: {result[0]} тенге.")
    else:
        print(f"Пользователь {name} не найден.")

    conn.close()

def withdraw(name, amount):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT balance FROM users WHERE name = ?
    ''', (name,))
    result = cursor.fetchone()

    if result:
        current_balance = result[0]
        if current_balance >= amount:
            new_balance = current_balance - amount
            cursor.execute('''
            UPDATE users SET balance = ? WHERE name = ?
            ''', (new_balance, name))
            conn.commit()
            print(f"Вы успешно вывели {amount} тенге. Ваш новый баланс: {new_balance} тенге.")
        else:
            print("Недостаточно средств для вывода.")
    else:
        print(f"Пользователь {name} не найден.")

    conn.close()


def main():
    clear_db()

    create_table()
    user_name = "Рустем"
    create_account(user_name)

    while True:
        print("\nМеню:")
        print("1. Работа (Заработать деньги)")
        print("2. Баланс")
        print("3. Выйти")
        print("4. Вывод средств")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            work(user_name)  
        elif choice == '2':
            check_balance(user_name) 
        elif choice == '3':
            print("До свидания!")
            break
        elif choice == '4':
            try:
                amount = float(input("Введите сумму для вывода: "))
                if amount <= 0:
                    print("Сумма вывода должна быть положительной.")
                else:
                    withdraw(user_name, amount) 
            except ValueError:
                print("Пожалуйста, введите корректную сумму.")
        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию от 1 до 4.")

if __name__ == "__main__":
    main()
