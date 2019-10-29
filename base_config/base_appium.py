#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : zhangxiaoping

import unittest
from selenium import webdriver


class Base_appium(unittest.TestCase):
    '''初始化设置'''
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'nox'  # 夜神
        desired_caps['app'] = 'com.taobao.taobao'
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass