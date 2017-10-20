import pytest
import os.path
import json

from Fixtures.application import Application
from Fixtures.users import Users

application = None
users_accounts = None

@pytest.fixture()
def app(request):
    global application
    # Loading config file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")) as f:
        config = json.load(f)
    # Creating fixture
    if application is None:
        platform = request.config.getoption("--platform") # platform is set from comand line
        print(platform)
        print(config['server'])
        application = Application(platform, config['server'])
    yield application
    # Everything here will be executed as teardown
    # application.destroy()

@pytest.fixture(scope='session')
def users(request):
    global users_accounts
    users_accounts = Users()
    users_accounts.get_users_from_db(request.config.getoption("--platform"))
    print(users_accounts)
    yield users_accounts
    # Everything here will be executed as teardown
    users_accounts.save_users_to_db()
    users_accounts.db_helper.close_connection()

def pytest_addoption(parser):
    parser.addoption("--platform", action="store")