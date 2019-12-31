# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 15:08
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : study_session_request.py
"""
两种
"""

import requests
session=requests.sessions.session()
# 登录
params = {"mobilephone": "15810447878", "pwd": "123456"}
resp=session.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)
# 充值
params = {"mobilephone": "15810447878", "amount": "1000"}
resp1=session.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
print(resp1.status_code)
print(resp1.text)
print(resp1.cookies)

session.close()

