#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : zhangxiaoping
"""HTMLTestRunner 截图版示例 selenium 版"""

from test_case.longin import Login


class Test_case(Login):

    def test_list(self):
        '''用例列表'''
        self.home_page()

