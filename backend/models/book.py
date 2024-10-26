def create_book(conn, title):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title) VALUES (%s)", (title,))
    conn.commit()
    cursor.close()

def get_all_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    return books