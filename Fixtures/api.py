import os.path
import requests

from PageObject.api_helpers import ApiHelpers
from Model.ApiRequest import ApiRequest

class Api:
    def __init__(self, server_url):
        # self.url = server_url
        self.url = 'https://core-master-core-master.phrend.net/users/sign_in.json'
        self.request = None

        self.helper = ApiHelpers()

    def get_json_scheme(self, scheme_name):
        project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
        return os.path.join(project_dir, "Support/JSON_scheme/{}.json".format(scheme_name))

    def create_request(self):
        self.request = ApiRequest()
        self.request.headers["Content-Type"] = "application/json"
        self.request.headers["Accept"] = "application/json"

    def add_body(self, body):
        if body is not None:
            self.request.body = body

    def add_headers(self, headers):
        if headers is not None:
            self.request.headers.update(headers)

    def send_request(self, url, type, headers=None, body=None):
        uri = "{}{}".format(self.url, url)

        self.add_body(body)
        self.add_headers(headers)

        print(self.request.body)
        print(self.request.headers)

        # return requests.post(uri, self.request.headers, self.request.headers)

        if type.upper() == 'GET':
            return requests.get(uri, self.request.headers)
        elif type.upper() == 'POST':
            return requests.post(uri, self.request.headers, self.request.body)
        elif type.upper() == 'PUT':
            return requests.put(uri, self.request.headers, self.request.body)
        elif type.upper() == 'DELETE':
            return requests.delete(uri, self.request.headers, self.request.body)
        else:
            raise "No method defined"
