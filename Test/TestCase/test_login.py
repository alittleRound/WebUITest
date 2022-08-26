# -*- coding:utf-8 -*-
# @Time    : 2022/08/26 09:03
# @Author  : wyt
# @Remark:

import os

from selenium import webdriver
import pytest
from Common.get_yaml_data import get_data
from Test.PageObject.login_page import LoginScenario
from Common.get_yaml_config import get_url




project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 找到当前项目的目录
test_data_path = project_path + '/Data/test_login.yaml'
# 读登录测试用例的数据
data = get_data(test_data_path)



@pytest.mark.parametrize(('username', 'pwd', 'status'), data)
class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 初始化driver对象
        config_path = project_path+'/Config/test_address.yaml'
        url = get_url(config_path)
        # 读取配置文件的url
        self.driver.get(url)

    def teardown(self):
        self.driver.quit()

    def test_login(self, username, pwd, status):
        LoginScenario(self.driver).login(username, pwd)
        if status == 0:
            # 登录失败
            errmsg = LoginScenario(self.driver).login_operation.get_errmsg()
            assert errmsg == '用户名或密码错误'
        elif status == 1:
            # 登录成功
            username = LoginScenario(self.driver).login_operation.get_login_user()
            assert username == '管理员'
        else:
            print('登录状态只能是0或1')


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
