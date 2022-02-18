import os

import allure
import pytest
from utils.log_util import log

from conf.conf_path import DATA_DIR
from cases.case_member.member_case import MemberCase
from utils.ymal_util import YamlUtil
case_data_path = os.path.join(DATA_DIR, 'member_case_data.yaml')
datas = YamlUtil(case_data_path).read()

@allure.feature('人员')
class TestMember(MemberCase):
    # conf_mysql = MemberCase().mysql_conf

    @allure.story('登录')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['login'])
    def test_login(self, data):
        """登录功能验证"""
        result = self.login_api(**data['account']).json()
        self.assert_equal(data['expected']['code'], result['code'])
        self.assert_equal(data['expected']['msg'], result['msg'])
        log.info('用例通过！')

