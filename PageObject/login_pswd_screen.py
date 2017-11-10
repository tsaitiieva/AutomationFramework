from PageObject.page import Page


class LoginPassword(Page):
    def __init__(self, app):
        super().__init__(app)

    def wait_page_to_load(self):
        self.wait_element_to_load('xpath', self.app.locators['passwordScreen_password_textfield'])

    def password_textfield(self):
        return self.find_element('xpath', self.app.locators['passwordScreen_password_textfield'])

    def lets_go_btn(self):
        return self.find_element('xpath', self.app.locators['passwordScreen_letsgo_button'])

    def enter_password(self, password):
        self.password_textfield().send_keys(password)
