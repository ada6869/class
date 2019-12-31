# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 13:55
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : http_request.py
import requests
from API.API_7.common.config import config

class HTTPRequest:
    """
    公共使用一个session，cookies自动传递
    使用这类的request方法去完成不同的http请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies=None):
        method=method.upper()#将method强制转成大写

        if type(data)==str:
            data=eval(data) #str转成字典

        if method =='GET':
            resp=requests.get(url,params=data,cookies=cookies)# resp是response对象
        elif method == 'POST':
            if json is not None:
                resp=requests.post(url, json=json,cookies=cookies)
            else:
                resp=requests.post(url, data=data,cookies=cookies)
        else:
            resp=None
            print('UN-support-method')
        return resp

class HTTPRequest2:
    """
    使用这类的request方法去完成不同的http请求，并且返回响应结果
    """
    def __init__(self):
        #打开一个session
        self.session =requests.sessions.session()

    def request(self,method,url,data=None,json=None):
        method=method.upper()#将method强制转换成全大写

        if type(data)==str:
            data=eval(data) #str转成字典
        #拼接url
        url = config.get('api','pre_url') + url
        print('请求url：',url)
        print('请求data：',data)


        if method=="GET":
            resp=self.session.request(method=method,url=url,params=data)
        elif method=='POST':
            if json is not None:
                resp = self.session.request(method=method,url=url, json=json)
            else:
                resp = self.session.request(method=method,url=url,data=data)
        else:
            resp= None
            print('UN-support-method')
            print('请求response：', resp.text)
        return resp
    def close(self):
        self.session.close()#用完记得关闭



if __name__=="__main__":
    params={"mobilephone":"15810447878","pwd":"123456"}
    http_request=HTTPRequest()
    #调用注册
    resp1 = http_request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/register', data=params)
    print(resp1.status_code)
    print(resp1.text)
    print(resp1.cookies)
    # 调用登录
    resp2 = http_request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login',
                         data=params)
    print(resp2.status_code)
    print(resp2.text)
    print(resp2.cookies)
    #调用充值
    params = {"mobilephone": "15810447878", "amount": "1000"}
    resp3 = http_request.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                         data=params, cookies=resp2.cookies)
    print(resp3.status_code)
    print(resp3.text)
    print(resp3.cookies)

    http_request2 = HTTPRequest2()
    #登录
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    resp4=http_request2.request('POST','http://test.lemonban.com/futureloan/mvc/api/member/login',
                         data=params)
    # 充值
    params = {"mobilephone": "15810447878", "amount": "1000"}
    resp5 =http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge',
                          data=params)
    print(resp4.status_code)
    print(resp4.text)
    print(resp4.cookies)
    print(resp5.status_code)
    print(resp5.text)
    print(resp5.cookies)