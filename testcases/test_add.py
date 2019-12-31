# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 14:46
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : test_add.py
import unittest
from API.API_8.common.http_request import HTTPRequest2
from API.API_8.common import do_excel
from API.API_8.common import contants
from ddt import ddt,data
from API.API_8.common.config import config
from API.API_8.common import context

@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'add')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_add(self, case):
        # print(case.title)
        case.data=str(case.data)#变成字典

        #参数化  配置文件中与测试用例中进行参数化配置
        # if case.data.__contains__('mobilephone') and case.data['mobilephone']=='normal_user':
        #     case.data['mobilephone']=config.get('data','normal_user')#拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd')  and case.data['pwd']=='normal_pwd':
        #     case.data['pwd']=config.get('data','normal_pwd')#拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('memberId')  and case.data['memberId']=='loan_member_id':
        #     case.data['memberId']=config.get('data','loan_member_id')#拿到配置文件里面的值赋值给mobilephone
        #在请求之前替换参数化的值
        case.data=context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

