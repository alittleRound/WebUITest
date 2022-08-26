# -*- coding:utf-8 -*-
# @Time    : 2022/08/26 09:00
# @Author  : wyt
# @Remark: 需要根据自己项目的实际元素修改定位方法

from Base.base import Base

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def find_username(self):
        """
        查找并返回用户名输入框元素
        :return:
        """
        ele = Base(self.driver).get_element('name', 'username')
        return ele

    def find_pwd(self):
        """
        查找并返回密码输入框元素
        :return:
        """
        ele = Base(self.driver).get_element('name', 'password')
        return ele

    def find_login_btn(self):
        """
        查找并返回登录按钮元素
        :return:
        """
        ele = Base(self.driver).get_element('id', 'login-btn')
        return ele


    def find_login_name(self):
        """
        查找并返回当前登录用户元素
        :return:
        """
        ele = Base(self.driver).get_element('class name', 'textHiddenSingle')
        return ele

    def find_errmsg(self):
        """
        查找登录错误信息元素
        :return:
        """
        ele = Base(self.driver).get_element('xpath','//*[@id="root"]/div/div/div[1]/div[2]/div[2]/div[2]/span[2]')
        return ele

class LoginOperation:
    def __init__(self, driver):
        """
        调用定位元素的类
        :param driver:
        :return:
        """
        self.login_page = LoginPage(driver)

    def input_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_pwd(self, pwd):
        """
        输入密码
        :param pwd:
        :return:
        """
        self.login_page.find_pwd().clear()
        self.login_page.find_pwd().send_keys(pwd)

    def click_login_btn(self):
        """
        点击登录
        :return:
        """
        self.login_page.find_login_btn().click()

    def get_login_user(self):
        """
        获取当前登录用户名
        :return:
        """
        self.login_page.find_logo().click()
        ele = self.login_page.find_login_name()
        return ele.text

    def get_errmsg(self):
        """
        获取登录错误文本
        :return:
        """
        return self.login_page.find_errmsg().text

class LoginScenario:
    def __init__(self, driver):
        self.login_operation = LoginOperation(driver)

    def login(self, username, pwd):
        self.login_operation.input_username(username)
        self.login_operation.input_pwd(pwd)
        self.login_operation.click_login_btn()
