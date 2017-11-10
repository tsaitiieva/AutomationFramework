import os.path
import requests
import json


from Model.ApiRequest import ApiRequest
from PageObject import api_helpers


class Api:
    def __init__(self, helper, server_url):
        self.helper = helper
        self.url = server_url
        self.request = None

    def get_json_scheme(self, scheme_name):
        path_to_scheme = os.path.join(self.helper.root_path, "Support/JSON_scheme/{}.json".format(scheme_name))
        with open(path_to_scheme, 'r') as scheme:
            return json.load(scheme)

    def add_parameters(self, users, api_helpers_method, user, args):
        """
        Call method from api_helpers with specified arguments and use its result as request data
        """
        method_to_call = getattr(api_helpers, 'return_{}'.format(api_helpers_method))

        if user is None and len(args) == 0:
            self.request.add_data(method_to_call())
        elif user is None:
            self.request.add_data(method_to_call(args))
        elif user is not None and len(args) == 0:
            self.request.add_data(method_to_call(users.accounts[user]))
        else:
            self.request.add_data(method_to_call(users.accounts[user], args))

    def create_request_with_default_headers(self):
        self.request = ApiRequest()
        self.request.headers["content-type"] = "application/json"

    def send_request(self, url, type, headers=None, params=None, data=None):
        uri = "{}{}".format(self.url, url)

        self.request.add_headers(headers)
        self.request.add_params(params)
        self.request.add_data(data)

        if type.upper() == 'GET':
            self.helper.attach_file('Headers', self.request.headers)

            return requests.get(uri, headers=self.request.headers)
        elif type.upper() == 'PUT':
            self.helper.attach_file('Headers', self.request.headers)
            self.helper.attach_file('Parameters', self.request.params)
            self.helper.attach_file('Data', self.request.data)

            return requests.put(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        elif type.upper() == 'POST':
            self.helper.attach_file('Headers', self.request.headers)
            self.helper.attach_file('Parameters', self.request.params)
            self.helper.attach_file('Data', self.request.data)

            return requests.post(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        elif type.upper() == 'DELETE':
            self.helper.attach_file('Header', self.request.headers)
            self.helper.attach_file('Parameters', self.request.params)
            self.helper.attach_file('Data', self.request.data)

            return requests.delete(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        else:
            raise ValueError('No method defined')
