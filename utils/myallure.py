import allure


def add_data(case_id, case_title, case_severity):
    allure_case_tag = f'{case_id}_{case_title}'
    allure.dynamic.title(case_title)  # 用例标题
    allure.dynamic.tag(allure_case_tag)  # 用例标签
    allure.dynamic.severity(case_severity)  # 用例严重级别


def add_request(request_obj):
    allure.attach(body=str(request_obj.request.url), name="请求地址",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(request_obj.request.headers), name="请求头",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(request_obj.request.body), name="请求body",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(request_obj.status_code), name="响应状态码",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(request_obj.headers), name="响应头", attachment_type=allure.attachment_type.TEXT)
    allure.attach(body=str(request_obj.text), name="响应body", attachment_type=allure.attachment_type.TEXT)
