

def return_sign_in_user(user_info):
    return {"user": {
                    "email": user_info.email,
                    "password": user_info.password
        }
        }