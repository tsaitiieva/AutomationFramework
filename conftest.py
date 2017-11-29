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


PLATFORMS = ('Android', 'iOS', 'API')
SERVERS = ('qa', 'prod')


def read_option(request):
    #Loading options from terminal
    options = {}

    platform = request.config.getoption("--platform")
    if platform is None:
        raise ValueError(
            'No platform has been transferred. Please specify pltform in the following way: --platform=[platform]')

    required_platform = get_required_option(platform, PLATFORMS)
    if required_platform is None:
        raise ValueError('Platform {0} is unknown. Please specify one of the following: {1}'.format(platform, PLATFORMS))
    options['platform'] = required_platform

    server = request.config.getoption("--server")
    if server is None:
        raise ValueError('No server has been transferred. Please specify server in the following way: --server=[server]')

    required_server = get_required_option(server, SERVERS)
    if required_server is None:
        raise ValueError('Server {0} is unknown. Please specify one of the following: {1}'.format(server, SERVERS))
    options['server'] = required_server

    return options


def read_config():
    # Loading config file
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")) as f:
        return json.load(f)


def get_required_option(option, options):
    for possible_option in options:
        if option.lower() == possible_option.lower():
            return possible_option
    return None


def get_server_options(server):
    config_options = read_config()
    return config_options['servers'][server]


@pytest.fixture(scope='session')
def helper():
    global support_helper
    if support_helper is None:
        support_helper = Helper()
    yield support_helper


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


@pytest.fixture()
def app(request, helper):
    options = read_option(request)
    if options['platform']=='Android' or options['platform']=='iOS':
        global ui_helper
        if ui_helper is None:
            ui_helper = Application(helper, session, options['platform'], get_server_options(options['server']))
        yield ui_helper
        # Everything here will be executed as teardown


@pytest.fixture()
def api(request, helper, session):
    options = read_option(request)
    if options['platform']=='API':
        global api_helper
        api_helper = Api(helper, session, get_server_options(options['server']))
        yield api_helper


def pytest_addoption(parser):
    parser.addoption("--platform", action="store")
    parser.addoption("--server", action="store")
