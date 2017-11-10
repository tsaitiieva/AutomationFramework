import sqlite3
import os.path

class DatabaseHelper:
    def __init__(self):
        # Initialize DB connection
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Support/Accounts.db")
        print(db_path)
        self.db_connection = sqlite3.connect(db_path)

    def save_changes(self):
        self.db_connection.commit()

    def close_connection(self):
        self.db_connection.close()

    def execute_query(self, query):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
