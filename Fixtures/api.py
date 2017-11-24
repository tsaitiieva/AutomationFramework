import os.path
import requests
import json


from Model.ApiRequest import ApiRequest
from PageObject import api_helpers


class Api:
    def __init__(self, helper, session, server_url):
        self.helper = helper
        self.session = session
        self.url = server_url
        self.request = None

    def get_json_scheme(self, scheme_name):
        path_to_scheme = os.path.join(self.helper.root_path, "Support/JSON_scheme/{}.json".format(scheme_name))
        with open(path_to_scheme, 'r') as scheme:
            return json.load(scheme)

    def add_parameters(self, api_helpers_method, user, args):
        """
        Call method from api_helpers with specified arguments and use its result as request data
        """
        method_to_call = getattr(api_helpers, 'return_{}'.format(api_helpers_method))

        if user is None and len(args) == 0:
            self.request.add_data(method_to_call())
        elif user is None:
            self.request.add_data(method_to_call(args))
        elif user is not None and len(args) == 0:
            self.request.add_data(method_to_call(self.session.users[user]))
        else:
            self.request.add_data(method_to_call(self.session.users[user], args))

    def create_request_with_default_headers(self):
        self.request = ApiRequest()
        self.request.headers["content-type"] = "application/json"

    def send_request(self, url, type, headers=None, params=None, data=None, cookies=None):
        uri = "{}{}".format(self.url, url)

        if self.request is None:
            self.create_request_with_default_headers()

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
            raise ValueError('No method defined')
