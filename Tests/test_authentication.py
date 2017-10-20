import time
from Steps import Authentication


def test_authentication_with_valid_credentials(app, users):
    Authentication.verify_that_landing_screen_is_displayed_correctly(app)
    Authentication.choose_login_on_landing_screen(app)
    # Authentication.change_domain(app, '')
    # Authentication.enter_login_and_continue()
    # Authentication.enter_password_and_continue()

