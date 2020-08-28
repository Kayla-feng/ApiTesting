import requests

class BaseApi:
    url = ""
    params = {}
    headers = {"accept":"application/json"}
    data = {}
    json = {}
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
                data=self.data,
                json=self.json
                     )
        return self

    def extract(self,field):
        value = getattr(self.response, field)
        return value


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
