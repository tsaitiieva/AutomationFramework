
import time

def verify_that_landing_screen_is_displayed_correctly(app):
    app.landing_screen.wait_page_to_load()
    assert app.landing_screen.get_title_text() == 'Swipe less, flirt more.'
    assert app.landing_screen.get_sign_up_btn() is not None
    assert app.landing_screen.get_login_btn() is not None


def choose_login_on_landing_screen(app):
    app.landing_screen.wait_page_to_load()
    app.landing_screen.choose_login()


def change_domain(app, server_address):
    pass


def enter_login_and_continue(app, email_address):
    pass


def enter_password_and_continue(app, password):
    pass