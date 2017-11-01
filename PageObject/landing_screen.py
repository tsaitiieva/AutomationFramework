from PageObject.page import Page


class Landing(Page):
    def __init__(self, app):
        super().__init__(app)

    def wait_page_to_load(self):
        self.wait_element_to_load('xpath', self.app.locators['landingScreen_screen_name_staticText'])

    def title(self):
        return self.find_element('xpath', self.app.locators['landingScreen_screen_name_staticText'])

    def sign_up_btn(self):
        return self.find_element('xpath', self.app.locators['landingScreen_sign_up_button'])

    def login_btn(self):
        return self.find_element('xpath', self.app.locators['landingScreen_login_button'])

    def get_title_text(self):
        return self.get_element_text(self.title())
