from peewee import *

class DatabaseHelper:
    db_sqlite = None

    def link_with_sqlite_db(path):
        DatabaseHelper.db_sqlite = SqliteDatabase(path)
        return DatabaseHelper.db_sqlite


class BaseSQLiteUsersModel(Model):
    class Meta:
        database = DatabaseHelper.db_sqlite
