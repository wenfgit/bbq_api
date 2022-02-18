# -*- coding: utf-8 -*-

# import json
# import traceback
# from datetime import datetime
# import inspect
import functools
# from utils.log_util import log
import json

from utils.log_util import log


def api_call(func):
    """
    接口调用记录
    :param func: 装饰的函数
    :return:
    """

    def inner(*args, **kwargs):
        log.info(f"开始调用接口：{func.__name__}")
        res = func(*args, **kwargs)
        log.info(f"结束调用接口：{func.__name__}")
        return res

    return inner

#
# def assert_param_non_null(*args, **kwargs):
#     b1 = True
#     if args:
#         for a in args:
#             if not a:
#                 b1 = False
#                 break
#     b2 = True
#     if kwargs:
#         for m in kwargs:
#             if not m:
#                 b2 = False
#                 break
#
#     return b1 and b2
#
#
# def param_null_not_execute(func):
#     """判断传入的参数是否为空,空则不执行"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if assert_param_non_null(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         msg = f"执行{func.__name__}出现异常: 参数是 {args} {kwargs}, 有参数为空"
#         raise RuntimeError(msg)
#
#     return wrapper
#
#
# def catch_and_log_exception(func):
#     """捕获并记录异常 """
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except (Exception, RuntimeError, TypeError, NameError, AttributeError, Warning) as e:
#             log.error("执行方法[%s]出现异常:%s,参数是: %s%s" % (func.__name__, e, args, kwargs))
#             log.error(traceback.print_exc())
#
#     return wrapper
#
#
# def deprecated(tips: str = None):
#     """声明该方法 已经被废弃 将不会被执行"""
#     @functools.wraps(func)
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             if str:
#                 log.warning("该方法已被弃用,不会被执行,%s." % tips)
#
#             raise RuntimeWarning("该方法已被弃用,不会被执行.")
#
#         return inner_wrapper
#
#     return wrapper
#
#
# def log_cost_time(func):
#     """记录耗时时间"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         log.debug("程序开始执行,任务执行结束后,将输出任务执行时间...")
#         start_time = datetime.now()
#         func(*args, **kwargs)
#         end_time = datetime.now()
#         cost_time = (end_time - start_time).seconds
#         log.debug(f"执行完了, 此次任务, 耗时：{cost_time} 秒")
#
#     return wrapper
#
#
# def params_type_verify(func):
#     """检查入参类型的装饰器"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(func)
#         params = sig.parameters
#         # 处理kwargs：字典
#         for k, v in kwargs:
#             param = params[k]
#             if param.annotation != inspect._empty and not isinstance(v, param.annotation):
#                 raise TypeError('方法%s的参数%s需要是%s类型的, 但是传入的是%s类型' % (func.__name__, k, param.annotation, type(v)))
#         # 处理args：元组
#         for i, x in enumerate(args):
#             param = list(params.values())[i]
#             if param.annotation != inspect._empty and not isinstance(x, param.annotation):
#                 raise TypeError('方法%s的参数%s需要是%s类型的, 但是传入的是%s类型' % (func.__name__, param.name, param.annotation, type(x)))
#         ret = func(*args, **kwargs)
#         return ret
#
#     return wrapper
#
#
# def json_convert(func):
#     """将被装饰函数的返回结果转换成JSON格式"""
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         try:
#             json_res = json.dumps(result)
#         except:
#             log.debug('接口未返回错误！')
#             return False
#         else:
#             return json_res
#
#     return wrapper
