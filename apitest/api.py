import requests

class BaseApi:
    url = ""
    params = {}
    headers = {"accept":"application/json"}
    json = {}
    data = {}
    method = "GET"

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
        value = self.response

        for _key in key.split("."):
            # print("value----",_key,value,type(value),expected_value)

            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value,_key)

            elif isinstance(value,(requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]

        assert value == expected_value
        return self
