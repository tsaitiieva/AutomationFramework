class User:
    def __init__(self, user_parameters):
        (self.id, self.email, self.password, self.name) = user_parameters
        self.session_id = None

    def add_core_session(self, session_id):
        self.session_id = session_id

    def __repr__(self):
        return 'id={}, email={}, password={}, name={}'.format(self.id, self.email, self.password, self.name)

