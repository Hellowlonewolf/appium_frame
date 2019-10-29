#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : zhangxiaoping
import time

from  base_config.base_appium import Base_appium




class Login(Base_appium):

    def home_page(self):
        '''登录用例'''
        self.setUpClass()
        time.sleep(2)
        #点击同意协议
        self.driver.find_element_by_id("com.taobao.taobao:id/uik_mdButtonDefaultPositive").click()
        time.sleep(3)
        #获取界面文本
        text = self.driver.find_element_by_id(u'com.taobao.taobao:id/tv_scan_text').text
        if text == '扫一扫':
            self.assertTrue(True)
            self.add_img()
            print('进入首页成功')
        else:
            self.assertTrue(False)
            self.add_img()
        assert text == '首页', '界面文本不为首页,当前界面文本为:%s' % text
        #点击搜索
        # self.driver.find_element_by_id("com.taobao.taobao:id/search_icon").click()