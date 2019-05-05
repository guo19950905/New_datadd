import json
import unittest

import requests
from parameterized import parameterized
from api.Login_Api import Login
def read_json():
    data = []
    with open('../data/login_data.json',encoding='utf-8') as f:
        my_data = json.load(f)
        for value in my_data.values():
            username = value.get('username')
            verify_code = value.get('verify_code')
            status_code = value.get('status_code')
            msg = value.get('msg')
            one = (username,verify_code,status_code,msg)
            data.append(one)
        return data

class TestHmLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()
        self.login = Login()

    def tearDown(self):
        self.session.close()

    def test_get_phone_code(self):
        ret = self.login.get_phone_code(self.session,'17635370834')
        self.assertIn('OK',ret.json().get('message'))

    @parameterized.expand(read_json())
    def test_hm_login(self,username,verify_code,status_code,msg):
        ret = self.login.hm_login(self.session,username,verify_code)
        print(ret.status_code)
        print(ret.json())