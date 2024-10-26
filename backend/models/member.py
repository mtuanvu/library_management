def create_member(conn, name, birthdate, address):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, birthdate, address) VALUES (%s, %s, %s)", (name, birthdate, address))
    conn.commit()
    cursor.close()

def get_all_members(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    cursor.close()
    return members