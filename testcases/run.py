# -*- coding: utf-8 -*- 
# @Time : 2019/12/25 16:58 
# @Author : Ada
# @File : run.py
import sys
sys.path.append('./')#project根目录地址
print(sys.path)


import unittest
from API.API_8.testcases import test_register
from API.API_8.testcases import test_login
from API.API_8.common import HTMLTestRunnerNew
from API.API_8.common import contants


# suite=unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTests(loader.loadTestsFromModule(test_register))
# suite.addTests(loader.loadTestsFromModule(test_login))

discover=unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

with open(contants.report_dir + '/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                           title="API test report",
                                           description="前程贷API",
                                           tester="mongo")

    runner.run(discover)