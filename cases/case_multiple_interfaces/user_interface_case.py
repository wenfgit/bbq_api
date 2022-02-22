import allure
from loguru import logger

from apis.api_excuse.user_api import UserApi
# from common.handle_mysql import HandleMysql

from cases.case_user.user_case import UserCase

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

