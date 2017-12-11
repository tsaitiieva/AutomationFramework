from Model.ApiRequest import ApiRequest
from jsonschema import validate
import allure


@allure.step("Create empty request without headers, data or parameters")
def create_empty_request(api):
    api.request = ApiRequest()


@allure.step("Create request with default headers")
def create_default_request(api):
    create_empty_request(api)
    api.request.headers["content-type"] = "application/json"


@allure.step("Create request with default headers and user's session cookies")
def create_default_request_with_user_session_cookies(api, user):
    create_default_request(api)
    if api.session.users[user].session_id is None:
        raise ValueError("Session id for user {0} is undefined".format(user))
    api.request.add_cookies(dict(phrendly_session=api.session.users[user].session_id))


@allure.step("Add request(s) to request")
def add_request_headers(api, headers):
    if api.request is None:
        raise ValueError("Request is None. You should create request first.")
    api.request.add_headers(headers)


@allure.step("Add cookies to request")
def add_request_cookies(api, cookies):
    if api.request is None:
        raise ValueError("Request is None. You should create request first.")
    api.request.add_cookies(cookies)


@allure.step("Add parameter(s) to request")
def add_request_parameters(api, params):
    if api.request is None:
        raise ValueError("Request is None. You should create request first.")
    api.request.add_params(params)


@allure.step("Add data to request")
def add_request_data(api, data):
    """
        Data should be transferred already converted to correct format (json, xml etc.)
    """
    if api.request is None:
        raise ValueError("Request is None. You should create request first.")
    api.request.add_data(data)


@allure.step("Add data to request using predefined method")
def add_request_data_from_api_helpers(api, api_helpers_method=None, user=None, *parameters):
    """
        Calls method from api_helpers class and adds its result as request data. Methods in api_helpers responsible for
        converting data to correct format.
    """
    api.add_request_data(api_helpers_method, user, parameters)


@allure.step("Send request to url")
def send_request_to_url(api, request_type, url, headers=None, params=None, data=None, cookies=None):
    response = api.send_request(request_type, url, headers, params, data, cookies)
    api.request.add_response(response)


@allure.step("Verify that response code is correct")
def verify_that_response_code_is_correct(api, code):
    response_code = api.request.get_response_code()
    api.helper.attach_file('Actual Response', api.request.response)
    
    assert response_code == code


@allure.step("Verify that response match json schema")
def verify_that_response_match_json_schema(api, shmene_name):
    response_body = api.request.get_response_body()
    json_scheme = api.get_json_scheme(shmene_name)

    api.helper.attach_file('Response', response_body)
    api.helper.attach_file('Json Scheme', json_scheme)

    validate(response_body, json_scheme)


@allure.step("Save response data to users session instance")
def save_response_param_to_user_data(api, response_param, user):
    response_param = api.request.get_response_body()[response_param]
    api.session.users[user].add_core_session(response_param)


def save_response_param_to_session_data(api, param):
    pass





