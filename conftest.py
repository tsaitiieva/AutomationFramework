import pytest
import os.path
import json
import allure

from Fixtures.application import Application
from Fixtures.session import Session
from Fixtures.api import Api
from Fixtures.helper import Helper

ui_helper = None
api_helper = None

session_helper = None
support_helper = None


def read_option(request):
    #Loading options from terminal
    options = {}
    try:
        platform = request.config.getoption("--platform")
        if platform.lower() == 'android':
            options['platform'] = 'Android'
        elif platform.lower() == 'ios':
            options['platform'] = 'iOS'
        elif platform.lower() == 'api':
            options['platform'] = 'API'
        else:
            raise ValueError('Unknown platform')
    except:
        raise ValueError('No platform has been tranfered. Please specify pltform in the following way: --platform=[platform]')

    return options


def read_config():
    # Loading config file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")) as f:
        return json.load(f)


@pytest.fixture(scope='session')
def helper():
    global support_helper
    if support_helper is None:
        support_helper = Helper()
    yield support_helper


@pytest.fixture()
def app(request, helper):
    options = read_option(request)
    if options['platform']=='Android' or options['platform']=='iOS':
        global ui_helper
        config = read_config()
        if ui_helper is None:
            ui_helper = Application(helper, session, options['platform'], config['server'])
        yield ui_helper
        # Everything here will be executed as teardown


@pytest.fixture()
def api(request, helper, session):
    options = read_option(request)
    if options['platform']=='API':
        global api_helper
        config = read_config()
        api_helper = Api(helper, session, config['server'])
        yield api_helper


@pytest.fixture(scope='session')
def session(request):
    global session_helper
    if session_helper is None:
        session_helper = Session()
        options = read_option(request)
        session_helper.get_users_from_db(options['platform'])
    yield session_helper
    # Everything here will be executed as teardown
    session_helper.db_helper.save_changes()
    session_helper.db_helper.close_connection()


def pytest_addoption(parser):
    parser.addoption("--platform", action="store")