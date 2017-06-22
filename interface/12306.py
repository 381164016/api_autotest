# -*- coding: utf-8 -*-
import imp
import sys

import time
from select import select

from selenium.webdriver.support.select import Select

imp.reload(sys)

import unittest
from selenium import webdriver



class usermessageTest(unittest.TestCase):
    """
    个人信息
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="https://kyfw.12306.cn/otn/login/init"
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_usermessage(self):
        """个人信息测试"""

        # ----------------------------------------login-------------------------------------------------
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_id("username").send_keys("381164016@qq.com")
        driver.find_element_by_id("password").send_keys("ZHcc530")
        time.sleep(25)
        driver.find_element_by_id("loginSub").click()
        time.sleep(2)
        driver.get("https://kyfw.12306.cn/otn/queryOrder/init")
        time.sleep(3)
        Select(driver.find_element_by_xpath(".//*[@id='use_G']/select")).select_by_value("2")
        driver.find_element_by_xpath(".//*[@id='querymyorderbutton']/label").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='checkbox_EA24174172']").click()
        driver.find_element_by_xpath(".//*[@id='many_resign_ids_EA24174172']").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='checkbox_mwOd4ustGS']").click()
        driver.find_element_by_xpath(".//*[@id='query_ticket']").click()
        time.sleep(3)
        num=driver.find_element_by_xpath(".//*[@id='YW_4100000T560D']").text
        for i in range(1,999999999999):
            if int(num)>0:
                driver.find_element_by_xpath(".//*[@id='submitOrder_id']").click()
                break
            else:
                driver.find_element_by_xpath(".//*[@id='query_ticket']").click()
                time.sleep(3)


