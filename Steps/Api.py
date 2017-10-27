from jsonschema import validate


def create_request_and_get_required_parameters(api, users, api_helpers_method, user):
    api.create_request()
    print(users.accounts)
    api.add_body(api.helper.return_sign_in_user(users.accounts[user]))


def send_post_request_to_url(api, url):
    # method_to_call = getattr(foo, 'bar')
    # result = method_to_call()
    response = api.send_request(url, 'post')
    api.request.add_response(response)


def verify_that_response_code_is_correct(api, code):
    assert api.response.code == code


def verify_that_response_match_json_schema(api, shmene_name):
    validate(api.response.body, api.get_json_scheme(shmene_name))


