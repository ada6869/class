# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 14:30
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : test_recharge.py
import unittest
from API.API_7.common.http_request import HTTPRequest2
from API.API_7.common import do_excel
from API.API_7.common import contants
from ddt import ddt,data
from API.API_7.common.do_mysql import DoMysql

@ddt
class RechargeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_recharge(self,case):
        print(case.title)
        #请求之前，判断一下是否需要sql
        if case.sql is not None:
            sql=eval(case.sql)['sql1']
            member=self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            before=member['leaveamount']

        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code=resp.json()['code']
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
            # 成功之后，判断一下是否需要sql
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member["leaveamount"])
                after = member["leaveamount"]
                recharge_amount = int(eval(case.data)['amount'])  #充值金额
                self.assertEqual(before + recharge_amount, after)
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()


