import json

import pytest
import requests
import logging
import jsonpath
from hamcrest import *


class TestRequest:

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("test_request")
    logger.setLevel(logging.INFO)
    url = 'https://testerhome.com/api/v3/topics.json?limit=2'

    @pytest.mark.skip
    def test_get(self):
        r = requests.get(self.url)
        TestRequest.logger.info(r)
        logging.info('--分割线--')
        logging.info(r.text)
        logging.info('--分割线--')
        logging.info(json.dumps(r.json(),indent=4))

    @pytest.mark.skip
    def test_post(self):
        p = requests.post(self.url,data={"a":"1","b":"f+b"},
                          headers={"a":"header","b":"c"})
        logging.info(p.url)
        logging.info(p)

    @pytest.mark.skip
    def test_cookies(self):
        r = requests.get("http://47.95.238.18:8890/cookie",cookies={"a":"aa","b":"string"})
        logging.info(r.text)

    def test_quote(self):
        url = 'http://test.wxapi.galaxy-immi.com/backend/liveactivity/livelist?page=1&page_size=10&total=0'
        r = requests.get(url,
                         # params = {"page":"1","page_size":"10","total":"0"},
                         headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
                                    "Referer": "http://test.wxadmin.galaxy-immi.com/Page_Activity/LiveDataList",
                                    "Origin":"http://test.wxadmin.galaxy-immi.com",
                                    "token":"ZswVy1bwlX6dTrjte21zFRrgcduopH86K3gv2WOiRk3n+Ju9rGTWJtZ1NPvg6SDLakJBLYFhih0Yxc96A7x71fDFHUnc8FpO/FcNkw1KY/F2AFtj/HpiVmBeYRcm3snJPkc+m3ib5bdMS7oIgxN/TX5oZ+tALGU="})
        re = json.dumps(r.json(),ensure_ascii=False,indent=2)
        # print(re)
        # assert r.json()["data"][0]["id"] == "97"
        # print(jsonpath.jsonpath(r.json(),"$.data[0].id"))
        id_list = jsonpath.jsonpath(r.json(),"$.data[?(@.title=='订单测试')]..id")
        # assert id_list[0] == '94'
        assert_that(["94","97"],has_item(id_list[0]))
        assert_that(["94","97"],any_of(
                has_item(id_list[0]),
                has_item("96")))
