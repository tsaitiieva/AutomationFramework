import os.path
import requests


from Model.ApiRequest import ApiRequest

class Api:
    def __init__(self, server_url):
        self.url = server_url
        # self.url = 'https://core-master-core-master.phrend.net'
        self.request = None

    def get_json_scheme(self, scheme_name):
        project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
        path_to_scheme = os.path.join(project_dir, "Support/JSON_scheme/{}.json".format(scheme_name))
        with open(path_to_scheme, 'r') as scheme:
            return scheme.read()

    def create_request(self):
        self.request = ApiRequest()
        self.request.headers["content-type"] = "application/json"
        # self.request.headers["Accept"] = "application/json"

    def send_request(self, url, type, headers=None, params=None, data=None):
        uri = "{}{}".format(self.url, url)

        self.request.add_headers(headers)
        self.request.add_params(params)
        self.request.add_data(data)

        # return requests.post(uri, self.request.headers, self.request.headers)

        if type.upper() == 'GET':
            return requests.get(uri, headers=self.request.headers)
        elif type.upper() == 'PUT':
            return requests.put(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        elif type.upper() == 'POST':
            return requests.post(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        elif type.upper() == 'DELETE':
            return requests.delete(uri, headers=self.request.headers, params=self.request.params, data=self.request.data)
        else:
            raise ValueError('No method defined')
