from jsonschema import validate
import allure


@allure.step("Create request with required parameters")
def create_request_with_required_parameters(api, users, api_helpers_method=None, user=None, *parameters):
    """
    Create request with defual headers, if api_helpers_method is transefered addtitional data will be attached to request
    """
    api.create_request_with_default_headers()
    if api_helpers_method is not None:
        api.add_parameters(users, api_helpers_method, user, parameters)


@allure.step("Send request to url")
def send_request_to_url(api, request_type, url):
    response = api.send_request(url, request_type)
    api.request.add_response(response)


@allure.step("Verify that response code is correct")
def verify_that_response_code_is_correct(api, code):
    assert api.request.response_code == code


@allure.step("Verify that response match json schema")
def verify_that_response_match_json_schema(api, shmene_name):
    validate(api.request.response, api.get_json_scheme(shmene_name))


