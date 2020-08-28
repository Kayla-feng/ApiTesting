from apitest.httpbin import *

# def test_version():
#     from apitest import __version__
#     assert isinstance(__version__,str)


def test_http_get():
    HttpGet()\
        .run()\
        .validate("status_code", 200)


def test_http_post():
    HttpPost().run()\
        .validate("status_code", 200)\
        .validate("headers.Server","gunicorn/19.9.0")\
        .validate("json().url","http://www.httpbin.org/post")\
        .validate("json().headers.Host","www.httpbin.org")


def test_httpbin_extract():
    status_code = HttpGet()\
        .run()\
        .extract("status_code")
    assert status_code == 200

def test_httpbin_parameters_extract():
     pass