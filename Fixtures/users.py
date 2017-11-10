from Fixtures.database import DatabaseHelper
from Model.User import User

class Users:
    """
    All users read from DB and stored in accounts dictionary with:
    key = some user identifier (e.g. male_account_with_credit_card)
    value = User class instance with all required user info (email, pswd, name)
    """

    def __init__(self):
        # Initialize database helper class
        self.db_helper = DatabaseHelper()
        self.accounts = {}


    def get_users_from_db(self, platform):
        query = "query to get users from DB"

        db_users = self.db_helper.execute_query(query)
        for user in db_users:
            self.accounts[user[0]] = User(user[1:])

    def save_users_to_db(self):
        pass

    def __repr__(self):
        result = ''
        for key in self.accounts:
            result += '{}: {}/n'.format(key, self.accounts[key])
        return result






