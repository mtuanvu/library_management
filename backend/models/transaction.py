from datetime import date


def create_transaction(conn, member_id, book_id, borrow_date, status):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (member_id, book_id, borrow_date, status) VALUES (%s, %s, %s, %s)", (member_id, book_id, borrow_date, status))
    conn.commit()
    cursor.close()

def get_transactions_report(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT members.name, members.birthdate, members.address, books.title, transactions.borrow_date, transactions.status
        FROM transactions
        JOIN members ON transactions.member_id = members.id
        JOIN books ON transactions.book_id = books.id
    """)
    report = cursor.fetchall()
    cursor.close()
    return report

def get_today_transactions(conn):
    cursor = conn.cursor()
    today = date.today()
    query = """
        SELECT m.name, m.birthdate, m.address, b.title, t.borrow_date, t.status
        FROM transactions t
        JOIN members m ON t.member_id = m.id
        JOIN books b ON t.book_id = b.id
        WHERE t.borrow_date = %s
    """
    cursor.execute(query, (today,))
    transactions = cursor.fetchall()
    cursor.close()
    return transactions