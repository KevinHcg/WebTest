# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : test_login.py
# Describe : 测试用例执行

import time
import unittest
from selenium import webdriver
from common.host_url import *
from pageObject.login.login_page import LoginPage
from testData.login.login_data import *
from common.decorator_ddt import ddt,data

# 用例编写步骤
# 1、创建文件
# 2、创建类
# 3、创建方法
# 用例夹具Fixtrue

@ddt
class TestLogin(unittest.TestCase):
    '''登录页面'''
    @classmethod
    def setUpClass(cls):
        print("=======================登录测试开始=======================")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.lg=LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("=======================登录测试结束=======================")
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.driver.refresh()

    def tearDown(self) -> None:
        time.sleep(1)

    @data(*login_data_01)
    def test_login_01(self,item):
        '''测试账号输入框'''
        self.lg.login(item['name'], item['pwd'])
        try:
            self.assertEqual(item['expected_result'], self.lg.chick_name_pwd())
        except AssertionError as e:
            print('断言错误：{}'.format(e))
            self.add_img()
            raise e

    @data(*login_data_02)
    def test_login_02(self, item):
        '''测试密码输入框'''
        self.lg.login(item['name'], item['pwd'])

        try:
            self.assertEqual(item['expected_result'], self.lg.chick_name_pwd())
        except AssertionError as e:
            self.add_img()
            print('断言错误：{}'.format(e))
            raise e

    @data(*login_data_03)
    def test_login_03(self,item):
        '''正常登录'''
        self.lg.login(item['name'],item['pwd'])
        try:
            self.assertEqual(item['expected_result'], self.lg.login_cg())
        except AssertionError as e:
            self.add_img()
            print('断言错误：{}'.format(e))
            raise e
if __name__ == '__main__':
    unittest.main()