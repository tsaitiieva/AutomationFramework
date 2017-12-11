import json


def return_sign_in_user(user_info):
    result = {"user": {
                    "email": user_info.email,
                    "password": user_info.password
        }
        }
    return json.dumps(result)
