from apitest.api import BaseApi

# def test_version():
#     from apitest import __version__
#     assert isinstance(__version__,str)



class HttpGet(BaseApi):

    url = "http://www.httpbin.org/get"
    method = "GET"


class HttpPost(BaseApi):

    url = "http://www.httpbin.org/post"
    method = "post"


def test_http_get():
    HttpGet().run().validate("status_code", 200)


def test_http_post():
    HttpPost().run().validate("status_code", 200)
