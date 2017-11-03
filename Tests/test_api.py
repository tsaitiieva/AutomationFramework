from Steps import Api
import pytest
import allure
from flaky import flaky
from random import randint
from jsonschema import validate
import json


@allure.issue('http://jira.lan/browse/ISSUE-3')
def test_sign_in_valid_credentials(api, users):
    with pytest.allure.step('Api.create_request_and_get_required_parameters'):
        Api.create_request_and_get_required_parameters(api, users, api_helpers_method='sign_in_user', user='seeded_male')
    with pytest.allure.step(' Api.send_post_request_to_url'):
        Api.send_post_request_to_url(api,'/users/sign_in.json')
    with pytest.allure.step('Api.verify_that_response_code_is_correct'):
        Api.verify_that_response_code_is_correct(api, 201)
    with pytest.allure.step(' Api.verify_that_response_match_json_schema'):

        Api.verify_that_response_match_json_schema(api, 'sign_in')

@pytest.allure.testcase('http://my.tms.org/TESTCASE-1')
def test_blank_pass():
    pass

@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_minor():
    assert False


@allure.feature('Feature1')
@allure.story('Story1')
def test_major():
    step()
    assert False


@allure.step('some operation for bar={0}')
def step():
    pass

@flaky(max_runs=3, min_passes=2)
@pytest.mark.label
def test_something_that_usually_passes():
    if randint(0,1)== 1:
        pass
    else:
        assert False
