import os.path
import allure
import logging


class Helper:
    """Helper class with some useful methods.
    You can work with its methods by calling its instance from api or app fixtures
    """

    def __init__(self):
        self.root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")

        # Initialize logger
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            handlers=[logging.FileHandler(os.path.join(self.root_path, "Logfile.log")),
                                      logging.StreamHandler()])
        self.logger = logging.getLogger("Logger")

    def log(self, logging_string):
        self.logger.info(logging_string)

    def attach_file(self, filename, content):
        allure.attach(filename, str(content))

    def attach_screenshot(self, driver):
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
