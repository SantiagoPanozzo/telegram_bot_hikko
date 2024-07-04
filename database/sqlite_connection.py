import sqlite3


class SqliteConnection:
    def __init__(self):
        self.database_name = "database/bot_hikko.db"
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.define_data()

    def define_data(self):
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                user_id INTEGER PRIMARY KEY NOT NULL,
                latitude REAL DEFAULT 0,
                longitude REAL DEFAULT 0,
                count INTEGER DEFAULT 0
            )
            """
        )

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetchall(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetchone(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()

    def __del__(self):
        self.connection.close()
