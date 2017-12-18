
from peewee import *
from Fixtures.database import BaseSQLiteUsersModel


class User(BaseSQLiteUsersModel):
    #user + platform should be unique combination
    user = CharField()
    email = CharField()
    password = CharField()
    name = CharField()
    platform = CharField(null=True)
    session = CharField(null=True)

    def __repr__(self):
        return 'User {} with email={}, password={}, name={}, platform={}, session={}'.format(self.user, self.email,
                                                                                             self.password, self.name, self.platform, self.session)

