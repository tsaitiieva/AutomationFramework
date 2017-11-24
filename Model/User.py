class User:
    def __init__(self, user_parameters):
        (self.id, self.email, self.password, self.name) = user_parameters
        self.core_session = None

    def add_core_session(self, core_session):
        self.core_session = core_session

    def __repr__(self):
        return 'id={}, email={}, password={}, name={}'.format(self.id, self.email, self.password, self.name)

