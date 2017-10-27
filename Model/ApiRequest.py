class ApiRequest:

    def __init__(self):
        self.headers = {}
        self.body = None

        self.response_code = None
        self.response = None


    def add_response(self, response):
        self.response_code = response.status_code
        self.response = response.json()