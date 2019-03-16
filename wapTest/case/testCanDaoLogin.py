# coding:utf-8
import ddt
import time
import unittest
from selenium import webdriver
from common.Utils import Utils
from common.Judge import Judge
from selenium.webdriver.common.by import By
from pageElement.candaoPageElement import candao
from common.excelUtil import excelUtil
excelUtil = excelUtil()
logindata = excelUtil.getData()
@ddt.ddt
class testCanDaoLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Utils = Utils(self.driver)
        self.candao = candao(self.driver)
        self.Utils.getUrl("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")

    @ddt.data(*logindata)
    def test_candao_login(self,data):
        result = self.candao.candao_page_element(data["username"],data["password"])
        self.assertEqual(result,data["expect"])


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()