import os.path
import allure


def attach_file(filename, content):
    allure.attach(filename, content)
