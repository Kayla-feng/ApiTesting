import requests

class BaseApi:
    url = ""
    params = {}
    headers = {"accept":"application/json"}
    json = {}
    data = {}
    method = "GET/post"

    def param(self,**params):
        self.params = params
        return self

    def set_data(self,data):
        self.data = data
        return self

    def run(self):
        self.response =requests.request(
                self.method,
                self.url,
                params=self.params,
                headers=self.headers,
                json=self.json,
                data=self.data
                     )
        return self

    def validate(self,key,expected_value):
        actual_value = getattr(self.response,key)
        assert actual_value == expected_value
        return self
