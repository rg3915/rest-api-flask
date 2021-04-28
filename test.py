import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'admin', '1234')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'regis', 'lçkjlj'),
    (3, 'huguinho', 'oiuyt')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit()
connection.close()
