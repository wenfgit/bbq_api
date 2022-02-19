from decimal import Decimal

import allure
from loguru import logger

from apis.api_excuse.user_api import UserApi
# from common.handle_mysql import HandleMysql


class UserCase(UserApi):

    @allure.step('step:调用业务api-注册')
    def case_register(self, data):
        """
        注册业务场景
        :param data:
        :return:
        """
        if data['phoneAndEmail'] == '$phone':
            data = self.template(data, {'phone': self.random_phone()})
        elif data['phoneAndEmail'] == '$email':
            data = self.template(data, {'email': self.random_email()})
        res = self.register_api(**data).json()
        return res

    @allure.step('step:调用业务api-自动登陆')
    def case_automaticLogin(self, data):
        """
        自动登陆业务场景
        :param data:
        :return:
        """
        if data['access-token'] == '$access-token':
            data = self.template(data, {'access-token': self.get_login_data()})
        res = self.automaticLogin_api(**data).json()
        return res
