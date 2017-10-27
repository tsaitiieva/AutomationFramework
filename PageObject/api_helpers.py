
class ApiHelpers:
    # def __init__(self):
    #     pass

    def return_sign_in_user(self, user_info):
        return {"user":{
                    "email" : user_info.email,
                    "password" : user_info.password
        }
        }