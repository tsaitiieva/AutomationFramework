#TODO Fix this: from PageObject import * by moving all imports to init.py
from PageObject.page import Page
from PageObject.browse_screen import Browse
from PageObject.landing_screen import Landing
from PageObject.login_screen import Login

from appium import webdriver

import logging
import os.path
# import yaml
import csv


class Application:
    def __init__(self, platform_type, server_name):
        self.project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")

        desired_caps = {}
        if platform_type == 'Android':
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'Nexus 6 - emulator'
            desired_caps['app'] = os.path.join(self.project_dir, "Tools/app-debug.apk")
            server_url = 'http://127.0.0.1:4778/wd/hub'
        else:
            desired_caps['platformName'] = 'iOS'
            desired_caps['platformVersion'] = '11.0'
            desired_caps['deviceName'] = 'iPhone SE'
            desired_caps['app'] = os.path.join(self.project_dir, "Tools/Phrendly.app")
            server_url = 'http://127.0.0.1:4777/wd/hub'

        self.driver = webdriver.Remote(server_url, desired_caps)
        self.server_name = server_name
        self.platform = platform_type

        #Load locators
        # with open(os.path.join(self.project_dir, "Support/locators.yaml"), 'r') as f:
        #     self.locators = yaml.load(f)[self.platform]

        self.locators = {}
        with open(os.path.join(self.project_dir, "Support/locators.csv")) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.locators[row['Locator']] = row[platform_type]

        # Initialize logger
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            handlers=[logging.FileHandler(os.path.join(self.project_dir, "Logfile.log")), logging.StreamHandler()])
        self.logger = logging.getLogger("Logger")

        # Create page object instances
        self.browse_screen = Browse(self)
        self.landing_screen = Landing(self)
        self.login_screen = Login(self)


    def log(self, logging_string):
        self.logger.info(logging_string)


