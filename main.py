#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : zhangxiaoping
import unittest
from base_config.HTMLTestRunner_cn import HTMLTestRunner
from test_work.test_screenshot_appium import Test_case

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_case)
    runer = HTMLTestRunner(title="自动化测试报告", description="Demo", stream=open("report/sample_test_report_appium.html", "wb"),
                           verbosity=2, retry=1, save_last_try=True)
    runer.run(suite)
