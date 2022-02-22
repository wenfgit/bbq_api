import os
import allure
import pytest

from utils.log_util import log
from conf.conf_path import DATA_DIR
from cases.case_multiple_interfaces.user_interface_case import UserInterfaceCase
from utils.ymal_util import YamlUtil
case_data_path = os.path.join(DATA_DIR, 'multiple_interfaces_data.yaml')
datas = YamlUtil(case_data_path).read()

@allure.feature('多接口测试')
class TestRegisterLogin(UserInterfaceCase):
    # conf_mysql = MemberCase().mysql_conf

    @allure.story('用户接口')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['register_and_login'])
    def test_register_login(self, data):
        """注册&登录功能验证"""
        res_register,res_login = self.case_register_login(data['account'])
        self.assert_equal(data['expected']['code'], res_register['code'])
        self.assert_equal(data['expected']['codeMsg'], res_register['codeMsg'])
        self.assert_equal(data['expected']['code'], res_login['code'])
        self.assert_equal(data['expected']['codeMsg'], res_login['codeMsg'])
        log.info('用例通过！')

    @allure.story('用户接口')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['login_and_automaticLogin'])
    def test_login_automaticLogin(self, data):
        """登陆&自动功能验证"""
        res = self.case_login_automaticLogin(data['account'])
        self.assert_equal(data['expected']['code'], res['code'])
        self.assert_equal(data['expected']['codeMsg'], res['codeMsg'])
        log.info('用例通过！')

