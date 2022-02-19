import allure
from jsonpath import jsonpath

from common.base_api import BaseApi
from utils.wrappers import api_call

class UserApi(BaseApi):

    @api_call
    @allure.step('step:登陆')
    def login_api(self, phoneAndEmail=BaseApi().account['phoneAndEmail'], password=BaseApi().account['password']):
        """
        登陆接口
        :param phoneAndEmail: 登陆手机号或邮箱，默认值读取config.ymal配置文件
        :param password: 登陆手密码，默认值读取config.ymal配置文件
        :return:
        """
        api = self.conf_data['user_api']['login']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'phoneAndEmail': phoneAndEmail,
                'password': password
            }
        }
        response = self.send_http(data)
        return response

    @allure.step('step:调用获取登录结果api')
    def get_login_data(self, phoneAndEmail=BaseApi().account['phoneAndEmail'], password=BaseApi().account['password']):
        """
        提取登陆响应token
        :return:
        """
        response = self.login_api(phoneAndEmail, password)
        res = response.json()
        login_data = dict()
        login_data['token'] = self.get_token(response)
        return login_data

    @api_call
    def register_api(self, phoneAndEmail: str, password: str):
        """
        注册接口
        :param phoneAndEmail: 注册手机号或邮箱
        :param password: 注册密码
        :return:
        """
        api = self.conf_data['user_api']['register']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'phoneAndEmail': phoneAndEmail,
                'password': password,
            }
        }
        response = self.send_http(data)
        return response

    @api_call
    def automaticLogin_api(self, header):
        """
        通过token自动登陆接口
        :return:
        """
        api = self.conf_data['user_api']['automaticLogin']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers.update(header)
        }
        response = self.send_http(data)
        return response