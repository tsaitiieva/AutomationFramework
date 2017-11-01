from PageObject.page import Page


class Landing(Page):
    def __init__(self, app):
        super().__init__(app)

    # title = (MobileBy.XPATH, '//*[@text="Swipe less, flirt more."]')
    # sign_up_btn = (MobileBy.XPATH, '//*[@text="Sign Up"]')
    # login_btn = (MobileBy.XPATH, '//*[@text="Login"]')

    def wait_page_to_load(self):
        self.wait_element_to_load('xpath', self.app.locators['landingScreen_screen_name_staticText'])

    def get_title(self):
        print(self.app.locators['landingScreen_screen_name_staticText'])
        return self.app.driver.find_element_by_xpath(self.app.locators['landingScreen_screen_name_staticText'])

    def get_sign_up_btn(self):
        return self.app.driver.find_element_by_xpath(self.app.locators['landingScreen_sign_up_button'])

    def get_login_btn(self):
        return self.app.driver.find_element_by_xpath(self.app.locators['landingScreen_login_button'])

    def get_title_text(self):
        # return self.driver.find_element_by_xpath(self.locators['landingScreen_screen_name_staticText'])
        return self.get_element_text(self.get_title())

    def choose_sign_up(self):
        # return self.driver.find_element_by_xpath(self.locators['landingScreen_sign_up_button'])
        self.get_sign_up_btn().click()

    def choose_login(self):
        # return self.driver.find_element_by_xpath(self.locators['landingScreen_login_button'])
        self.get_login_btn().click()
