from jsonschema import validate
from PageObject import api_helpers


def create_request_and_get_required_parameters(api, users, api_helpers_method, user):
    api.create_request()
    method_to_call = getattr(api_helpers, 'return_{}'.format(api_helpers_method))
    # api.request.add_data(api.helper.return_sign_in_user(users.accounts[user]))
    print(users.accounts[user])
    user_info = users.accounts[user]
    api.request.add_data(method_to_call(users.accounts[user]))


def send_post_request_to_url(api, url):
    # method_to_call = getattr(foo, 'bar')
    # result = method_to_call()
    response = api.send_request(url, 'post')
    api.request.add_response(response)


def verify_that_response_code_is_correct(api, code):
    assert api.request.response_code == code


def verify_that_response_match_json_schema(api, shmene_name):
    print("Json scheme ===>")
    print(api.get_json_scheme(shmene_name))

    validate(api.request.response, api.get_json_scheme(shmene_name))


