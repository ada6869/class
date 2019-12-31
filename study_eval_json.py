# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 11:25
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : study_eval_json.py
# 数据类型的转换  str ---》dict

import json
# 正常的json格式
# {"key":[]}
params='{"status":0,"code":"20111","data":null,"msg":"登录成功"}'
p='{"mobile":"15810447878","pwd":None}'#请求入参  None是python里面的，null是java里面的
d=eval(p)
print(d)
# json.load()
# d=eval(params)#根据Python的数据类型来做转换
# print(d['status'])

d1=json.loads(params)
print(type(d1),d1['status'])


