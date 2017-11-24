from jsonschema import validate
import allure


@allure.step("Create request with required parameters")
def create_request_with_required_parameters(api, api_helpers_method=None, user=None, *parameters):
    """
    Create request with defual headers, if api_helpers_method is transefered addtitional data will be attached to request
    """
    api.create_request_with_default_headers()
    if api_helpers_method is not None:
        api.add_parameters(api_helpers_method, user, parameters)


@allure.step("Send request to url")
def send_request_to_url(api, request_type, url, headers=None, params=None, data=None, cookies=None):
    response = api.send_request(url, request_type, headers, params, data, cookies)
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


@allure.step("Save core session from response to users session instance")
def save_core_session_from_response(api, user):
    core_session = api.request.get_response_body()['session_id']
    api.session.users[user].add_core_session(core_session)


@allure.step("Use user's session in cookies")
def use_user_session_cookie(api, user):
    api.create_request_with_default_headers()
    api.request.add_cookies(dict(phrendly_session=api.session.users[user].core_session))




