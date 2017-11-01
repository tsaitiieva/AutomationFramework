import pytest
import os.path
import json

from Fixtures.application import Application
from Fixtures.users import Users
from Fixtures.api import Api

application = None
users_accounts = None
api_helper = None


def read_option(request):
    #Loading options from terminal
    options = {}
    platform = request.config.getoption("--platform")
    if platform.lower() == 'android':
        options['platform'] = 'Android'
    elif platform.lower() == 'ios':
        options['platform'] = 'iOS'
    elif platform.lower() == 'api':
        options['platform'] = 'API'
    else:
        raise ValueError('Unknown platform')

    return options


def read_config():
    # Loading config file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")) as f:
        return json.load(f)


@pytest.fixture()
def app(request):
    options = read_option(request)
    if options['platform']=='Android' or options['platform']=='iOS':
        global application
        config = read_config()
        if application is None:
            application = Application(options['platform'], config['server'])
        yield application
        # Everything here will be executed as teardown
        # application.destroy()


@pytest.fixture()
def api(request):
    options = read_option(request)
    if options['platform']=='API':
        global api_helper
        config = read_config()
        api_helper = Api(config['server'])
        yield api_helper


@pytest.fixture(scope='session')
def users(request):
    global users_accounts
    users_accounts = Users()
    options = read_option(request)
    users_accounts.get_users_from_db(options['platform'])
    print(users_accounts)
    yield users_accounts
    # Everything here will be executed as teardown
    users_accounts.save_users_to_db()
    users_accounts.db_helper.close_connection()


def pytest_addoption(parser):
    parser.addoption("--platform", action="store")