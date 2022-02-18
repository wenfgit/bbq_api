import allure
from jsonpath import jsonpath

from common.base_api import BaseApi
from utils.wrappers import api_call

class MemberApi(BaseApi):

    @api_call
    @allure.step('step:登陆')
    def login_api(self, phone=BaseApi().account['phone'], password=BaseApi().account['password']):
        """
        登录接口
        :return:
        """
        api = self.conf_data['member_api']['login']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'phone': phone,
                'password': password,
                'type': 2
            }
        }
        response = self.send_http(data)
        return response

    @allure.step('step:调用获取登录结果api')
    def get_login_data(self, user=BaseApi().account['phone'], pwd=BaseApi().account['password']):
        """
        提取处理登录响应数据，包括id、leave_amount、mobile_phone、reg_name

        :return:
        """
        response = self.login_api(user, pwd)
        res = response.json()
        login_data = dict()
        login_data['token'] = self.get_token(response)
        login_data['member_id'] = jsonpath(res, '$..id')[0]
        login_data['leave_amount'] = jsonpath(res, '$..leave_amount')[0]
        login_data['mobile_phone'] = jsonpath(res, '$..mobile_phone')[0]
        login_data['reg_name'] = jsonpath(res, '$..reg_name')[0]
        return login_data

    @api_call
    def register_api(self, mobile_phone: str, pwd: str, member_type: int, reg_name=None):
        """
        注册接口
        :param mobile_phone: 手机号
        :param pwd: 密码
        :param member_type: 0-管理员，1-普通会员，不传默认为1
        :param reg_name:注册名
        :return:
        """
        api = self.conf_data['member_api']['register']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'mobile_phone': mobile_phone,
                'pwd': pwd,
                'type': member_type,
                # 'reg_name': reg_name
            }
        }
        if reg_name:
            data['json']['reg_name'] = reg_name
        response = self.send_http(data)
        return response

    @api_call
    def recharge_api(self, member_id: int, amount: float, token):
        """
        账户充值接口
        :param member_id: 用户id
        :param amount: 充值金额（最多小数点后两位）
        :param token:
        :return:
        """
        api = self.conf_data['member_api']['recharge']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'member_id': member_id,
                'amount': amount
            }
        }
        data['headers'].update({'Authorization': token})
        response = self.send_http(data)
        return response

    @api_call
    def withdraw_api(self, member_id: int, amount: float, token):
        """
        账户提现接口
        :param member_id: 用户id
        :param amount: 提现金额（最多小数点后两位）
        :param token:
        :return:
        """
        api = self.conf_data['member_api']['withdraw']
        data = {
            'url': self.host + api,
            'method': 'post',
            'headers': self.headers,
            'json': {
                'member_id': member_id,
                'amount': amount
            }
        }
        # data['headers'].update({'Authorization': token})
        self.headers['Authorization'] = token
        response = self.send_http(data)
        return response

    @api_call
    def info_update_api(self, member_id: int, reg_name: str, token):
        """
        用户信息更新接口
        :param member_id:用户id
        :param reg_name:修改名称
        :param token:
        :return:
        """
        api = self.conf_data['member_api']['update']
        data = {
            'url': self.host + api,
            'method': 'patch',
            'headers': self.headers,
            'json': {
                'member_id': member_id,
                'reg_name': reg_name
            }
        }
        # data['headers'].update({'Authorization': token})
        self.headers['Authorization'] = token
        response = self.send_http(data)
        return response

    @api_call
    def get_user_info_api(self, member_id, token):
        """
        获取单个用户信息接口
        :param member_id:用户id
        :param token:
        :return:
        """
        data = {
            'url': self.host + f'/member/{member_id}/info',
            'method': 'get',
            'headers': self.headers,
        }
        self.headers['Authorization'] = token
        response = self.send_http(data)
        return response

