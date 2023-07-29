import sqlite3


class DBClass:
    def __init__(self, db_path: str = 'Database/db_bot.db'):
        self.db_path = db_path


    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql_query: str, parameters: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql_query, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table(self, table_name: str):
        sql_query = f'CREATE TABLE IF NOT EXISTS {table_name} (id PRIMARY KEY, name TEXT, age INT, comment TEXT)'
        self.execute(sql_query, commit=True)

    def create_new_user(self, parameters: tuple[str, int, str, str]):
        sql_query = 'INSERT INTO users (name, tg_id, login, password) VALUES (?, ?, ?, ?)'
        self.execute(sql_query, parameters, commit=True)

    @staticmethod
    def extract_kwargs(sql_query: str, parameters: dict) -> tuple:
        sql_query += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql_query, tuple(parameters.values())

    def find_user(self, table_name: str, **kwargs):
        sql_query = f'SELECT * FROM {table_name} WHERE '
        sql_query, parameters = self.extract_kwargs(sql_query, kwargs)
        self.execute(sql_query, parameters, fetchall=True)
