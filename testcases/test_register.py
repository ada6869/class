# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 14:30
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : test_register.py
import unittest
from API.API_6.common.http_request import HTTPRequest2
from API.API_6.common import do_excel
from API.API_6.common import contants
from ddt import ddt,data
from API.API_6.common import do_mysql
@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()
    @data(*cases)
    def test_register(self,case):
        if case.data.find('register_mobile') > -1:#判断参数化的标识
            sql='select max(mobilephone) from future.member'
            max_phone=self.mysql.fetch_one(sql)[0]#查询最大手机号码
            #最大手机号码+1
            max_phone=int(max_phone)+1
            #replace 方法是替换之后重新返回一个新的字符串
            case.data=case.data.replace('register_mobile',str(max_phone))#替换参数值

        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()

