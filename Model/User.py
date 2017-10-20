class User:
    def __init__(self, user_parameters):
        (self.id, self.email, self.password, self.name) = user_parameters

    def __repr__(self):
        return 'id={}, email={}, password={}, name={}'.format(self.id, self.email, self.password, self.name)

