# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : run.py
# Describe : 测试套件运行
# ---------------------------------------
import unittest
from common.ExquisiteTestReport import HTMLTestRunner
from common.SendReportToEmail import *



# 一、创建测试套件
suite = unittest.TestSuite()
# 二、创建用例加载器
lod = unittest.TestLoader()
# 三、将用例加载到测试套件

# 加载方式一、通过用例模块进行加载
# from testCase.login import test_login
# from testCase.memo import test_add_memo_case
# suite.addTests(lod.loadTestsFromModule(test_login))
# suite.addTests(lod.loadTestsFromModule(test_add_memo_case))

# 加载方式二、通过类名加载
# from testCase.login.test_login import TestLogin
# from testCase.memo.test_add_memo_case import TestAddMemo
# suite.addTests(lod.loadTestsFromTestCase(TestLogin))
# suite.addTests(lod.loadTestsFromTestCase(TestAddMemo))

# 加载方式三、通过用例所在路径进行加载
suite.addTests(lod.discover(r'./testCase'))

# 优化只用一行代码实现
# suite = unittest.defaultTestLoader.discover(r'./testCase')

title = '《测试工具综合平台》Web自动化测试报告'
with open(r'./report/'+title+'.html','wb') as f:
    runner = HTMLTestRunner(stream = f,verbosity=2,title = title,tester='iTest岗')
    runner.run(suite)

# 发送邮件
mail_host = ""  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 密码
# 邮件发送和接收人
# receiver = ['211986576@qq.com', '1205409349@qq.com', ]
# SendReportToEmail().send_report(title,mail_host,mail_user,mail_pass,receiver)

