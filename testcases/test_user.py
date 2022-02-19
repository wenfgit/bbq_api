import os

import allure
import pytest
from utils.log_util import log

from conf.conf_path import DATA_DIR
from cases.case_user.user_case import UserCase
from utils.ymal_util import YamlUtil
case_data_path = os.path.join(DATA_DIR, 'user_case_data.yaml')
datas = YamlUtil(case_data_path).read()

@allure.feature('用户')
class TestMember(UserCase):
    # conf_mysql = MemberCase().mysql_conf

    @allure.story('登录')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['login'])
    def test_login(self, data):
        """登录功能验证"""
        result = self.login_api(**data['account']).json()
        self.assert_equal(data['expected']['code'], result['code'])
        self.assert_equal(data['expected']['codeMsg'], result['codeMsg'])
        log.info('用例通过！')

    @allure.story('注册')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['register'])
    def test_register(self, data):
        """注册功能验证"""
        result = self.case_register(data['account'])
        self.assert_equal(data['expected']['code'], result['code'])
        self.assert_equal(data['expected']['codeMsg'], result['codeMsg'])
        log.info('用例通过！')

    @allure.story('自动登陆')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['automaticLogin'])
    def test_automaticLogin(self, data):
        """自动登陆功能验证"""
        result = self.case_automaticLogin(data['header'])
        self.assert_equal(data['expected']['code'], result['code'])
        self.assert_equal(data['expected']['codeMsg'], result['codeMsg'])
        log.info('用例通过！')

