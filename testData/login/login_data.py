# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : login_data.py
# Describe : 测试数据


#校验账号
login_data_01 =[
    {"case_name":"账号为空","name":"","pwd":"test123456","expected_result":"请输入账号！",},
    {"case_name":"账号不正确","name":"test007","pwd":"test123456","expected_result":"账号或密码错误",},
    {"case_name":"账号长度小于8位","name":"tttt","pwd":"test123456","expected_result":"长度在 8 到 20 个字符",},
    {"case_name":"账号长度大于20位","name":"testtesttest","pwd":"test123456","expected_result":"长度在 8 到 20 个字符",},
]

#校验密码
login_data_02 = [
    {"case_name":"密码为空","name":"test03","pwd":"","expected_result":"请输入密码！",},
    {"case_name":"密码不正确","name":"test03","pwd":"888","expected_result":"账号或密码错误",},
    {"case_name":"密码长度大于20字符","name":"test03","pwd":"1234567890123456789011","expected_result":"长度在 8 到 20 个字符",},
    {"case_name":"密码长度小于8字符","name": "test03", "pwd": "12345","expected_result":"长度在 8 到 20 个字符",},
]

#正确的账号和密码
login_data_03 =[{"case_name":"正确的账号和密码","name":"test","pwd":"test123456","expected_result":"欢迎访问造数平台"}]
