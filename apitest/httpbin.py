from apitest.base_api import BaseApi


class HttpGet(BaseApi):

    url = "http://www.httpbin.org/get"
    method = "GET"


class HttpPost(BaseApi):

    url = "http://www.httpbin.org/post"
    method = "post"