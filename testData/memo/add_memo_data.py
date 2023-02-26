# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : add_memo_data.py
# Describe : 测试数据

import random
d=str(random.randint(1,8))

add_memo_data_01=[
    {"case_name": "标题必填，校验不填标题提示是否正确", "name": "", "option": "li["+d+"]", 'des': '不填标题', "expected_result": "标题不能为空",},
    {"case_name": "描述内容必填，校验不填描述内容提示是否正确", "name": "不填描述内容", "option": "li["+d+"]", 'des': '', "expected_result": "内容不能为空", },
    {"case_name": "全部填写正确", "name": "全部填写正确", "option": "li[" + d + "]", 'des': '全部填写正确', "check": "全部填写正确",},
    {"case_name": "标题唯一，校验标题已存在是否能创建", "name": "全部填写正确", "option": "li[" + d + "]", 'des': '标题已存在', "expected_result": "标题已存在",},

]