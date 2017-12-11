import os.path
import requests
import json


from Model.ApiRequest import ApiRequest
from PageObject import api_helpers


class Api:
    def __init__(self, helper, session, server_options):
        self.helper = helper
        self.session = session
        self.url = server_options['url'] #TODO add check for empty URL
        self.request = None

    def add_request_data(self, api_helpers_method, user, args):
        """
        Call method from api_helpers with specified arguments and use its result as request data
        """
        if self.request is None:
            raise ValueError("Request is None. You should create request first.")
        if api_helpers_method is None:
            raise ValueError("No api helpers method name has been transferred. Please specify method name.")

        method_to_call = getattr(api_helpers, 'return_{}'.format(api_helpers_method))
        if user is None and len(args) == 0:
            self.request.add_data(method_to_call())
        elif user is None:
            self.request.add_data(method_to_call(args))
        elif user is not None and len(args) == 0:
            self.request.add_data(method_to_call(self.session.users[user]))
        else:
            self.request.add_data(method_to_call(self.session.users[user], args))

    def send_request(self, type, url, headers=None, params=None, data=None, cookies=None):
        uri = "{}{}".format(self.url, url)

        if self.request is None:
            self.request = ApiRequest()

        self.request.add_headers(headers)
        self.request.add_params(params)
        self.request.add_data(data)
        self.request.add_cookies(cookies)

        self.helper.attach_file('Headers', self.request.headers)
        self.helper.attach_file('Parameters', self.request.params)
        self.helper.attach_file('Data', self.request.data)
        self.helper.attach_file('Cookies', self.request.cookies)

        if type.upper() == 'GET':
            return requests.get(uri, headers=self.request.headers, cookies=self.request.cookies)
        elif type.upper() == 'PUT':
            return requests.put(uri, headers=self.request.headers, params=self.request.params, data=self.request.data, cookies=self.request.cookies)
        elif type.upper() == 'POST':
            return requests.post(uri, headers=self.request.headers, params=self.request.params, data=self.request.data, cookies=self.request.cookies)
        elif type.upper() == 'DELETE':
            return requests.delete(uri, headers=self.request.headers, params=self.request.params, data=self.request.data, cookies=self.request.cookies)
        else:
            raise ValueError('Undefined method {0}'.format(type))

    def get_json_scheme(self, scheme_name):
        path_to_scheme = os.path.join(self.helper.root_path, "Support/JSON_scheme/{}.json".format(scheme_name))
        with open(path_to_scheme, 'r') as scheme:
            return json.load(scheme)
