import json


class ApiRequest:

    def __init__(self):
        self.headers = {}
        self.data = None
        self.params = None

        self.response_code = None
        self.response = None

    def add_response(self, response):
        self.response_code = response.status_code
        self.response = response.json()

    def add_headers(self, headers):
        if headers is not None:
            self.headers.update(headers)

    def add_params(self, params):
        if params is not None:
            self.headers.update(params)

    def add_data(self, data):
        if data is not None:
            self.data = json.dumps(data)