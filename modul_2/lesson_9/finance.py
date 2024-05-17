import sqlite3
import sys


def create_table():
    with sqlite3.connect('finance.db') as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            type TEXT,
            amount REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        con.commit()


def add_transaction(transaction_type, amount):
    with sqlite3.connect('finance.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO transactions (type, amount) VALUES (?, ?)', (transaction_type, amount))
        con.commit()


def calculate_balance():
    with sqlite3.connect('finance.db') as con:
        cur = con.cursor()
        cur.execute('SELECT SUM(amount) FROM transactions WHERE type = "earn"')
        total_earnings = cur.fetchone()[0] or 0
        cur.execute('SELECT SUM(amount) FROM transactions WHERE type = "spend"')
        total_spendings = cur.fetchone()[0] or 0
        return total_earnings - total_spendings


def main():
    if len(sys.argv) < 2:
        return

    command = sys.argv[1]

    if command == 'earn' and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        add_transaction('earn', amount)
        print(f"Earnt {amount}")
    elif command == 'spend' and len(sys.argv) == 3:
        amount = float(sys.argv[2])
        add_transaction('spend', amount)
        print(f"Spent {amount}")
    elif command == 'balance':
        balance = calculate_balance()
        print(f"Current balance: {balance}")
    else:
        print("Usage: python finance.py [earn|spend|balance] [amount]")


if __name__ == '__main__':
    create_table()
    main()
