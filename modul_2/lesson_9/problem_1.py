from sqlite3 import connect
import prettytable


def create_table():
    with connect('contacts.db') as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts(
            name VARCHAR(50),
            surname VARCHAR(50),
            phone VARCHAR(50)
        )
        ''')
        con.commit()


def list_contacts():
    with connect('contacts.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM contacts')
        contacts = cur.fetchall()
        table = prettytable.PrettyTable(['Name', 'Surname', 'Phone'])
        for contact in contacts:
            table.add_row(contact)
        print(table)


def search_contacts(name):
    with connect('contacts.db') as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM contacts WHERE name LIKE ?', (f'%{name}%',))
        contacts = cur.fetchall()
        table = prettytable.PrettyTable(['Name', 'Surname', 'Phone'])
        for contact in contacts:
            table.add_row(contact)
        print(table)


def add_contact(name, surname, phone):
    with connect('contacts.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO contacts (name, surname, phone) VALUES (?, ?, ?)', (name, surname, phone))
        con.commit()


def main():
    create_table()
    while True:
        print("\nContacts Command-line Application")
        print("1. List contacts")
        print("2. Search contacts")
        print("3. Add contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_contacts()
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contacts(name)
        elif choice == '3':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone: ")
            add_contact(name, surname, phone)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
