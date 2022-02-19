import os
import allure
import requests
from jsonpath import jsonpath

from utils.handle_assert import HandleAssert
from utils.log_util import log
from utils.ymal_util import YamlUtil
from utils import myallure

from common.utils import Utils
from conf.conf_path import CONF_DIR

class BaseApi(object):
    conf_path = os.path.join(CONF_DIR, 'config.yaml')
    # 配置文件数据
    conf_data = YamlUtil(conf_path).read()
    host = conf_data['env']['host']
    headers = conf_data['request_headers']['headers']
    account = conf_data['account']
    # investor_account = conf_data['investor_account']
    mysql_conf = conf_data['mysql']

    def send_http(self, data: dict):
        """
        发送http请求
        :param data: 请求数据
        :return:
        """
        try:
            self.__api_log(**data)
            response = requests.request(**data)
            log.info(f"响应状态码为：{response.status_code}")
        except Exception as e:
            log.error(f'发送请求失败，请求参数为：{data}')
            log.exception(f'发生的错误为：{e}')
            raise e
        else:
            myallure.add_request(response)
            return response

    # @staticmethod
    # def get_yaml(file_name):
    #     """
    #     读取yaml文件
    #     :param file_name: 文件路径名称
    #     :return: dict
    #     """
    #     return YamlUtil(file_name).read()

    @staticmethod
    def get_token(response):
        """
        处理并提取token
        :param response:
        :return:
        """
        return Utils.handle_token(response)

    @staticmethod
    @allure.step('step:数据替换')
    def template(source_data: str, data: dict):
        """
        替换数据
        :param source_data: 源数据
        :param data: 替换内容，如{data:new_data}
        :return:
        """

        return Utils.handle_template(source_data, data)

    # @staticmethod
    # def to_two_decimal(data):
    #     """
    #     将整数或浮点数转化为两位数decimal
    #     :param data:
    #     :return:
    #     """
    #     return Utils.handle_decimal(data)

    @staticmethod
    def random_phone():
        """
        生成随机手机号
        :return:
        """
        return Utils.handle_random_phone()

    @staticmethod
    def random_email():
        """
        生成随机邮箱
        :return:
        """
        return Utils.handle_random_email()

    @staticmethod
    def __api_log(method, url, headers=None, params=None, json=None):
        log.info(f"请求方式：{method}")
        log.info(f"请求地址：{url}")
        log.info(f"请求头：{headers}")
        log.info(f"请求参数：{params}")
        log.info(f"请求体：{json}")

    @staticmethod
    def assert_equal(ex, re):
        """
        断言相等
        :param ex:预期结果
        :param re:实际结果
        :return:
        """
        return HandleAssert.eq(ex, re)

    @staticmethod
    def assert_contains(content, target):
        """
        断言包含
        :param content: 文本内容
        :param target: 目标文本
        :return:
        """
        return HandleAssert.contains(content, target)

if __name__ == '__main__':
    a = BaseApi()
    # a.template()
