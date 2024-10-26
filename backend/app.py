from config import get_db_connection
from models.book import create_book, get_all_books
from models.member import create_member, get_all_members
from models.transaction import create_transaction, get_transactions_report, get_today_transactions
from datetime import date


def add_books():
    conn = get_db_connection()
    while True:
        title = input("Enter the title of the book: ")
        create_book(conn, title)
        another = input("Do you want to add another book? (y/n): ")
        if another.lower() != 'y':
            break
    conn.close()

def add_members():
    conn = get_db_connection()
    while True:
        name = input("Enter the name of the member: ")
        birthdate = input("Enter the birthdate (YYYY-MM-DD): ")
        address = input("Enter the address: ")
        create_member(conn, name, birthdate, address)
        another = input("Do you want to add another member? (y/n): ")
        if another.lower() != 'y':
            break
    conn.close()


def create_custom_transaction():
    conn = get_db_connection()
    members = get_all_members(conn)
    books = get_all_books(conn)

    if not members or not books:
        print("No members or books found. Please add some data first.")
        conn.close()
        return

    while True:
        print("\nAvailable Members:")
        for member in members:
            print(f"Member ID: {member[0]}, Name: {member[1]}")

        print("\nAvailable Books:")
        for book in books:
            print(f"Book ID: {book[0]}, Title: {book[1]}")

        member_id = input("Enter Member ID for the transaction: ")
        book_id = input("Enter Book ID for the transaction: ")

        status = input("Enter status (Borrowed/Returned): ")
        transaction_date = date.today().strftime('%Y-%m-%d')

        create_transaction(conn, member_id, book_id, transaction_date, status)
        print(f"Transaction created for Member ID: {member_id} with Book ID: {book_id} - Status: {status}")

        more = input("Do you want to create another transaction? (y/n): ")
        if more.lower() != 'y':
            break

    conn.close()
    print("Transactions created successfully.")


def print_report():
    conn = get_db_connection()
    report = get_transactions_report(conn)
    print(f"{'STT':<5}{'Tên Thành Viên':<20}{'Ngày Sinh':<15}{'Địa Chỉ':<25}{'Tên Sách':<20}{'Ngày Mượn':<15}{'Trạng Thái':<10}")
    for idx, (name, birthdate, address, title, borrow_date, status) in enumerate(report, start=1):
        birthdate_str = birthdate.strftime('%Y-%m-%d') if birthdate else "N/A"
        borrow_date_str = borrow_date.strftime('%Y-%m-%d') if borrow_date else "N/A"
        print(f"{idx:<5}{name:<20}{birthdate_str:<15}{address:<25}{title:<20}{borrow_date_str:<15}{status:<10}")
    conn.close()

def print_today_transactions():
    conn = get_db_connection()
    transactions = get_today_transactions(conn)
    if transactions:
        print(f"{'STT':<5}{'Tên Thành Viên':<20}{'Ngày Sinh':<15}{'Địa Chỉ':<15}{'Tên Sách':<20}{'Ngày Mượn':<15}{'Trạng Thái':<10}")
        for idx, (name, birthdate, address, title, borrow_date, status) in enumerate(transactions, start=1):
            birthdate_str = birthdate.strftime('%Y-%m-%d') if birthdate else "N/A"
            borrow_date_str = borrow_date.strftime('%Y-%m-%d') if borrow_date else "N/A"
            print(f"{idx:<5}{name:<20}{birthdate_str:<15}{address:<15}{title:<20}{borrow_date_str:<15}{status:<10}")
    else:
        print("No transactions found for today.")
    conn.close()

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Books")
        print("2. Add Members")
        print("3. Create Sample Transactions")
        print("4. Print Transactions Report")
        print("5. Print Today's Transactions")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_books()
        elif choice == '2':
            add_members()
        elif choice == '3':
            create_custom_transaction()
        elif choice == '4':
            print_report()
        elif choice == '5':
            print_today_transactions()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
