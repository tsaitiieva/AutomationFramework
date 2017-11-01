from Steps import Api


def test_sign_in_valid_credentials(api, users):
    Api.create_request_and_get_required_parameters(api, users, 'sign_in_user', 'seeded_male')
    Api.send_post_request_to_url(api,'/users/sign_in.json')
    Api.verify_that_response_code_is_correct(api, 201)
    Api.verify_that_response_match_json_schema(api, 'sign_in')