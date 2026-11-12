import sqlite3

connection = sqlite3.connect("helpdesk.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    problem TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

connection.commit()
connection.close()

def add_ticket(name, problem, priority):
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tickets (name, problem, priority, status)
        VALUES (?, ?, ?, ?)
    """, (name, problem, priority, "Open"))

    connection.commit()
    connection.close()

def get_tickets():
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def update_ticket_status(ticket_id, new_status):
     
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    """, (new_status, ticket_id))

    connection.commit()
    connection.close()