#TODO move all imports to init.py file
import time
from Steps import Authentication


def test_authentication_with_valid_credentials(app, users):
    user = users.accounts['seeded_male']
    Authentication.verify_that_landing_screen_is_displayed_correctly(app)
    Authentication.choose_login_on_landing_screen(app)
    Authentication.verify_that_email_login_screen_is_displayed_correctly(app)
    Authentication.change_domain(app, app.server)
    Authentication.enter_email_and_continue(app, user.email)
    Authentication.verify_that_pswd_login_screen_is_displayed_correctly(app)
    Authentication.enter_password_and_continue(app, user.password)


