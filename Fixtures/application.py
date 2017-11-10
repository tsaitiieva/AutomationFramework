from PageObject.landing_screen import Landing
from PageObject.login_pswd_screen import LoginPassword

from appium import webdriver


import os.path
# import yaml
import csv


class Application:
    def __init__(self, helper, platform_type, server):
        self.helper = helper

        desired_caps = {}
        if platform_type == 'Android':
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'Nexus 6 - emulator'
            desired_caps['app'] = os.path.join(self.helper.root_path, "Tools/[your app name]")
            server_url = 'http://127.0.0.1:4778/wd/hub'
        else:
            desired_caps['platformName'] = 'iOS'
            desired_caps['platformVersion'] = '11.0'
            desired_caps['deviceName'] = 'iPhone SE'
            desired_caps['app'] = os.path.join(self.helper.root_path, "Tools/[your app name]")
            server_url = 'http://127.0.0.1:4777/wd/hub'

        self.driver = webdriver.Remote(server_url, desired_caps)
        self.server = server
        self.platform = platform_type

        #Load locators from yaml file
        # with open(os.path.join(self.project_dir, "Support/locators.yaml"), 'r') as f:
        #     self.locators = yaml.load(f)[self.platform]

        # Load locators from csv file
        self.locators = {}
        with open(os.path.join(self.helper.root_path, "Support/locators.csv")) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.locators[row['Locator']] = row[platform_type]

        # Create page object instances
        self.landing_screen = Landing(self)
        self.login_pswd_screen = LoginPassword(self)

    def get_pagesource(self, filename):
        source = self.driver.page_source
        with open(os.path.join(self.helper.root_path, "/Temp/{}".format(filename)), 'a', encoding='utf-8') as f:
            f.write(source)


