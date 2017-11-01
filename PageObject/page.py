from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, app):
        self.app = app

    def get_element_text(self, element):
        if self.app.platform == 'iOS':
            return element.value
        else:
            return element.text

    def wait_element_to_load(self, locate_by, locator):
        locator_strategy = None
        if locate_by.lower() == 'xpath':
            locator_strategy = MobileBy.XPATH
        elif locate_by.lower() == 'id':
            locator_strategy = MobileBy.ID

        if locator_strategy is not None:
            WebDriverWait(self.app.driver, 30).until(EC.presence_of_element_located((locator_strategy, locator)))
        else:
            raise ValueError('Undefined locator strategy {}'.format(locate_by))

