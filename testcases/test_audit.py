# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 15:00
# @Software: PyCharm Community Edition
# @Author  : Ada
# @File    : test_audit.py

import unittest
from API.API_6.common.http_request import HTTPRequest2
from API.API_6.common import do_excel
from API.API_6.common import contants
from ddt import ddt,data

@ddt
class AuditTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'audit')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest2()

    @data(*cases)
    def test_audit(self,case):
        print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code=resp.json()['code']
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
