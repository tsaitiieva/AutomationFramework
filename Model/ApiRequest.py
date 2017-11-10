import json


class ApiRequest:
    def __init__(self):
        self.headers = {}
        self.data = None
        self.params = None

        self.response = None
        self.response_code = None
        self.response_body = None

    def add_response(self, response):
        self.response = response

    def get_response_code(self):
        if self.response is None:
            raise ValueError('Response is None')

        if self.response_code is None:
            self.response_code = self.response.status_code

        return self.response_code

    def get_response_body(self):
        if self.response is None:
            raise ValueError('Response is None')

        if self.response_body is None:
            self.response_body = self.response.json()

        return self.response_body

    def add_headers(self, headers):
        if headers is not None:
            self.headers.update(headers)

    def add_params(self, params):
        if params is not None:
            self.headers.update(params)

    def add_data(self, data):
        if data is not None:
            self.data = json.dumps(data)

    def clear_response(self):
        self.response_code = None
        self.response = None