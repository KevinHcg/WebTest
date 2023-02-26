# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : test_add_memo.py
# Describe : 测试用例执行

import time
import unittest
from selenium import webdriver
from common.host_url import *
from common.decorator_ddt import ddt,data
from pageObject.memo.add_memo_page import AddMemo
from testData.memo.add_memo_data import *
from pageObject.login.login_page import LoginPage


@ddt
class TestAddMemo(unittest.TestCase):
    '''添加备忘录'''
    @classmethod
    def setUpClass(cls):
        print("=======================添加备忘录测试开始=======================")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.lg=LoginPage(cls.driver)
        cls.lg.login('test','test123456')
        cls.am=AddMemo(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.am=AddMemo(cls.driver)
        cls.i=0
        while cls.i<=1:
            cls.i+=1
            cls.am.del_memo()
        print("=======================添加备忘录测试结束=======================")
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.driver.refresh()


    def tearDown(self) -> None:
        time.sleep(1)

    @data(*add_memo_data_01)
    def test_login_01(self,item):
        self.am.add_memo(item['name'], item['option'],item['des'])
        if '不填标题' in item['name']:
            try:
                self.assertEqual(item['expected_result'], self.am.check_name())
            except AssertionError as e:
                print('断言错误：{}'.format(e))
                self.add_img()
                raise e
        if '不填描述内容' in item['name']:
            try:
                self.assertEqual(item['expected_result'], self.am.check_des())
            except AssertionError as e:
                print('断言错误：{}'.format(e))
                self.add_img()
                raise e
        if '全部填写正确' in item['name']:
            try:
                self.assertEqual(item['expected_result'], self.am.check_t())
            except AssertionError as e:
                print('断言错误：{}'.format(e))
                self.add_img()
                raise e
        if '标题已存在' in item['name']:
            try:
                self.assertEqual(item['expected_result'], self.am.check_t())
            except AssertionError as e:
                print('断言错误：{}'.format(e))
                self.add_img()
                raise e


if __name__ == '__main__':
    unittest.main()