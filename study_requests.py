# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 14:16
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : study_requests.py
import requests

# 1.构造请求:请求方式、请求地址、请求参数
# 2.发起请求
# 3.返回响应
# 4.判断响应码，响应体

#注册接口
# params={"mobilephone":"15810447878","pwd":"123456"}
# resp=requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register',params=params)
# # resp是response对象
# print("响应码：",resp.status_code)
# print("响应文本：",resp.text)
# print("响应头：",resp.headers)
# print("响应cookie：",resp.cookies)
# print("响应cookie：",resp.request._cookies)

#登录接口
params={"mobilephone":"15810447878","pwd":"123456"}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',
                   data=params)#resp是response对象，如果是post则使用data传参
print("响应码：",resp.status_code)
print("响应文本：",resp.text)
print("响应cookie：",resp.cookies)
print("请求cookie：",resp.request._cookies)

# 充值接口
params={"mobilephone":"15810447878","amount":"1000"}
resp=requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                   data=params,cookies=resp.cookies)
print("响应码：",resp.status_code)
print("响应文本：",resp.text)
print("响应cookie：",resp.cookies)
print("请求cookie：",resp.request._cookies)
