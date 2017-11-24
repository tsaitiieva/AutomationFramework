from Steps import Api


def test_sign_in_valid_credentials(api):
    Api.create_request_with_required_parameters(api, 'sign_in_user', 'seeded_male')
    Api.send_request_to_url(api, 'post','/users/sign_in.json')
    Api.verify_that_response_code_is_correct(api, 201)
    Api.verify_that_response_match_json_schema(api, 'sign_in')
    Api.save_core_session_from_response(api, 'seeded_male')


def test_get_current_user_info(api):
    Api.use_user_session_cookie(api, 'seeded_male')
    Api.send_request_to_url(api, 'get', '/current_user.json')
    Api.verify_that_response_code_is_correct(api, 200)
    Api.verify_that_response_match_json_schema(api, 'current_user')