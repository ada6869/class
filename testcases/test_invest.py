# -*- coding: utf-8 -*-
# @Time    : 2019/12/6 14:27
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : test_invest.py
import unittest
from API.API_8.common.http_request import HTTPRequest2
from API.API_8.common import do_excel
from API.API_8.common import contants
from ddt import ddt,data
from API.API_8.common import context
from API.API_8.common import do_mysql
from API.API_8.common.config import config

@ddt
class InvestTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'invest')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()
    @data(*cases)
    def test_invest(self, case):
        print('开始执行测试用例：',case.title)
        case.data=str(case.data)#变成字典
       #在请求之前替换参数化的值
        case.data=context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()["code"])
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
            #判断加标成功之后，查询数据库，取到loan_id
            if resp.json()["msg"]=="加标成功":
                sql="SELECT id FROM future.loan WHERE memberid=88538 order by id desc limit 1"
                loan_id=self.mysql.fetch_one(sql)[0]
                print("标的ID:",loan_id)
                #保存到类属性里面
                setattr(context.Context,"loan_id",str(loan_id))
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

