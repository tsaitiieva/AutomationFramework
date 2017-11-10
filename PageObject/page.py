from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    """Basic class. All page object extemds this class.
    Add here all methods general for all pages such as swipe, scroll etc."""

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
        else:
            raise ValueError('Unknown locator strategy {}'.format(locate_by))

        WebDriverWait(self.app.driver, 30).until(EC.presence_of_element_located((locator_strategy, locator)))

    def find_element(self, locate_by, locator):
        if locate_by.lower() == 'xpath':
            return self.app.driver.find_element_by_xpath(locator)
        elif locate_by.lower() == 'id':
            return self.app.driver.find_element_by_id(locator)
        else:
            raise ValueError('Unknown locator strategy {}'.format(locate_by))


