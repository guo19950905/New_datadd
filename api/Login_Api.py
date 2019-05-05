

class Login:
    def __init__(self):
        self.get_phone_code_url = 'http://ttapi.research.itcast.cn/app/v1_0/sms/codes/'
        self.get_login_url = 'http://ttapi.research.itcast.cn/app/v1_0/authorizations'

    def get_phone_code(self,session,mobile):
        return session.get(self.get_phone_code_url + mobile)

    def hm_login(self,session,username,verify_code):
        my_json = {}
        if username:
            my_json['username'] = username
        if verify_code:
            my_json['verify_code'] = verify_code
        return session.post(self.get_login_url,json=my_json)