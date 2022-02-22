import allure
from loguru import logger

from apis.api_excuse.user_api import UserApi
# from common.handle_mysql import HandleMysql

from cases.case_user.user_case import UserCase

usercase =UserCase()

class UserInterfaceCase(UserApi):

    @allure.step('step:注册并登陆')
    def case_register_login(self, data):

        if data['phoneAndEmail'] == '$phones':
            data = self.template(data, {'phones': self.random_phone()})
        elif data['phoneAndEmail'] == '$emails':
            data = self.template(data, {'emails': self.random_email()})
        res_register = usercase.case_register(data)  #注册
        res_login = usercase.login_api(data)    #登陆
        return res_register,res_login

    @allure.step('step:登陆并自动登陆')
    def case_login_automaticLogin(self, data):

        res_login = usercase.get_login_data(**data)  # 登陆
        res_login['access-token'] = res_login.pop('token')
        res_automaticLogin = usercase.case_automaticLogin(res_login) #自动登陆
        return res_automaticLogin


