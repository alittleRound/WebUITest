# -*- coding:utf-8 -*-
# @Time    : 2022/08/26 08:53
# @Author  : wyt
# @Remark:

from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by, value, sec=20):
        """
        封装find_element方法，加上显示等待
        :param by: 定位器
        :param value: 定位值
        :param sec: 等待秒数
        :return: 如果找到元素则返回element对象，否则返回False
        """
        by_list = ['id', 'name', 'class name', 'tag name', 'link text', 'partial link text', 'xpath', 'css selector']
        if by not in by_list:
            raise NameError(
                "Locator Error: only 'id','name','class name','tag name','link text','partial link text','xpath','css selector' can be used")
        else:
            try:
                element = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_element(by=by, value=value))
                return element
            except Exception as e:
                raise e

    def get_elements(self, by, value, sec=60):
        """
        封装find_elements方法，加上显示等待
        :param by: 定位器
        :param value: 定位值
        :param sec: 等待秒数
        :return: 如果找到元素则返回elements对象，否则返回False
        """
        by_list = ['id', 'name', 'class name', 'tag name', 'link text', 'partial link text', 'xpath', 'css selector']
        if by not in by_list:
            raise NameError(
                "Locator Error: only 'id','name','class name','tag name','link text','partial link text','xpath','css selector' can be used")
        else:
            try:
                elements = WebDriverWait(self.driver, sec, 1).until(lambda x: x.find_elements(by=by, value=value))
                return elements
            except Exception as e:
                raise e
