from PageObject.page import Page
import time

class LoginEmail(Page):
    def __init__(self, app):
        super().__init__(app)

    def wait_page_to_load(self):
        self.wait_element_to_load('xpath', self.app.locators['loginScreen_email_textfield'])

    def email_textfield(self):
        return self.find_element('xpath', self.app.locators['loginScreen_email_textfield'])

    def domain_btn(self):
        return self.find_element('xpath', self.app.locators['loginScreen_domain_button'])

    def server_btn(self):
        return self.find_element('xpath', self.app.locators['loginScreen_domain_alert_server_core_button'])

    def continue_btn(self):
        return self.find_element('xpath', self.app.locators['loginScreen_continue_button'])

    def enter_email(self, email):
        self.email_textfield().send_keys(email)

    def change_domain(self):
        for x in range(0, 5):
            self.domain_btn().click()
        self.server_btn().click()

