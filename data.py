import sqlite3
import csv

patch=sqlite3.connect("charlie.db")
cursor=patch.cursor()

# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# # query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# # cursor.execute(query)
# # patch.commit()

# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/en_in/')"
# cursor.execute(query)
# patch.commit()

import sqlite3

patch = sqlite3.connect("charlie.db")
cursor = patch.cursor()

contacts = [
    ("champ", "7978696"),
    ("rohit", "6207359"),
    ("Ritik","875797")
    
]

def contact_exists(name, mobile_no):
    cursor.execute("SELECT COUNT(*) FROM contacts WHERE name = ? OR mobile_no = ?", (name, mobile_no))
    return cursor.fetchone()[0] > 0

def delete_contact(name, mobile_no):
    cursor.execute("DELETE FROM contacts WHERE name = ? AND mobile_no = ?", (name, mobile_no))
    print(f"Contact '{name}' with mobile number '{mobile_no}' has been deleted from the database.")

existing_contacts = cursor.execute("SELECT name, mobile_no FROM contacts").fetchall()

for db_contact in existing_contacts:
    db_name, db_mobile_no = db_contact
    if (db_name, db_mobile_no) not in contacts:
        delete_contact(db_name, db_mobile_no)

for contact in contacts:
    name, mobile_no = contact
    if not contact_exists(name, mobile_no):
        cursor.execute("INSERT INTO contacts (name, mobile_no) VALUES (?, ?)",(name, mobile_no))
    else:
        print(f"Contact '{name}' or mobile number '{mobile_no}' already exists.")

patch.commit()
patch.close()


# query = 'champ'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])