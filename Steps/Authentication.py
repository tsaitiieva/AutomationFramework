
def verify_that_landing_screen_is_displayed_correctly(app):
    app.landing_screen.wait_page_to_load()
    assert app.landing_screen.get_title_text() == 'Swipe less, flirt more.'
    assert app.landing_screen.sign_up_btn() is not None
    assert app.landing_screen.login_btn() is not None


def choose_login_on_landing_screen(app):
    app.landing_screen.wait_page_to_load()
    app.landing_screen.login_btn().click()


def verify_that_email_login_screen_is_displayed_correctly(app):
    app.login_email_screen.wait_page_to_load()
    assert app.login_email_screen.email_textfield() is not None
    assert app.login_email_screen.domain_btn() is not None
    assert app.login_email_screen.continue_btn() is not None


def change_domain(app, server_address):
    app.login_email_screen.change_domain()


def enter_email_and_continue(app, email_address):
    app.login_email_screen.wait_page_to_load()
    app.login_email_screen.enter_email(email_address)
    app.login_email_screen.continue_btn().click()


def verify_that_pswd_login_screen_is_displayed_correctly(app):
    app.login_pswd_screen.wait_page_to_load()
    assert app.login_pswd_screen.password_textfield() is not None
    app.get_pagesource("Pswd")
    assert app.login_pswd_screen.lets_go_btn() is not None


def enter_password_and_continue(app, password):
    app.login_pswd_screen.wait_page_to_load()
    app.login_pswd_screen.enter_password(password)
    app.login_pswd_screen.lets_go_btn().click()