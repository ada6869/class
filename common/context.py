# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 15:33
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : context.py
import re
from API.API_7.common.config import config
import configparser

class Context:
    loan_id = None


def replace(data):

    p = "#(.*?)#"  # 正则表达式

    while re.search(p,data):
        print(data)
        m = re.search(p,data)  # 从任意位置开始找，找第一个就返回Match_object,如果没有找None
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.get('data',g)  # 根据key取配置文件里面的值
        except configparser.NoOptionError as e:#如果配置文件里面的时候，去Context里面取
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print('找不到参数化的值')
                raise e

        print(v)
        # 记得替换后的内容，继续用data接收
        data = re.sub(p,v,data,count=1)  # 查找替换 count查找的次数

    return data