import sqlite3

connection = sqlite3.connect('Database/db_bot.db')
cursor = connection.cursor()


def create_users_table():
    sql = '''CREATE TABLE IF  NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR, login VARCHAR, password VARCHAR)'''
    cursor.execute(sql)
    connection.commit()
