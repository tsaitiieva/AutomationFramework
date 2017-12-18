from Fixtures.database import DatabaseHelper
from Model.User import User
from peewee import *


class Session:
    def __init__(self):
        # Initialize database helper class
        self.users_db = None
        self.users = {}

    def connect_to_db(self, path):
        # self.users_db = DatabaseHelper.link_with_sqlite_db(path)
        User._meta.database.init(path)
        self.users_db = User._meta.database
        self.users_db.connect()

    def close_db_connection(self):
        self.users_db.close()

    def populate_accounts_db(self):
        self.users_db.create_tables([User])

        #TODO I don't know where to put all these
        User.create(user='seeded_male', email='api_male_seeker1@a.com', password='12345678', name='api_male_seeker1', platform='Api')
        User.create(user='seeded_male', email='mobile_male_speaker3@a.com', password='12345678', name='mobile_male_speaker3', platform='iOS')
        User.create(user='seeded_male', email='api_male_seeker2@a.com', password='12345678', name='api_male_seeker2', platform='Android')
        User.create(user='seeded_female', email='api_female_speaker1@a.com', password='12345678', name='api_female_speaker1', platform='Api')
        User.create(user='seeded_female', email='mobile_female_receiver1@a.com', password='12345678', name='mobile_female_receiver1', platform='iOS')
        User.create(user='seeded_female', email='api_female_speaker2@a.com', password='12345678', name='api_female_speaker2', platform='Android')

    def get_users_from_db(self, platform):
        query = User.select().where(User.platform=='Api')

        for user in query:
            self.users[user.user] = user

    def save_users_to_db(self):
        for key in self.users:
            self.users[key].save()

    def __repr__(self):
        result = ''
        for key in self.users:
            result += '{}: {}/n'.format(key, self.users[key])
        return result






