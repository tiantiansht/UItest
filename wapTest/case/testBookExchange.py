# coding:utf-8
import time
import unittest
from selenium import webdriver
from common.Utils import Utils
from common.Judge import Judge
from selenium.webdriver.common.by import By
class testBookExchange(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Utils = Utils(self.driver)
        self.Judge = Judge(self.driver)
        self.Utils.getUrl("http://wap.cmread.com/nap/p/exchange_store.jsp")

    def test_book_exchange(self):
        self.assertEqual(self.Utils.getText((By.CSS_SELECTOR,"div.cmr-bookticket_exchange-title.co-font-large")),"书券兑换")
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//img[@class='tae-img lazy-really-loaded lazy-loaded']"),"src"))
        self.assertEqual(self.Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[1]/div[1]/p[1]")),"1元书券卡")
        self.assertEqual(self.Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[1]/div[1]/p[2]")),"充入账户后30天有效")
        self.Judge.is_presence_of_element((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[1]/div[1]/p[3]"))
        self.assertEqual(self.Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[1]/div[2]")),"兑换")
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[last()]/img"),"src"))
        self.assertEqual(self.Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[last()]/div[1]/p[1]")),"5元书券卡")
        self.assertEqual(self.Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[last()]/div[1]/p[2]")),"充入账户后30天有效")
        self.Judge.is_presence_of_element((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[last()]/div[1]/p[3]"))
        self.assertEqual(self.Utils.getText((By.XPATH, "//ul[@class='cmr-bookticket_exchange-lists']/li[last()]/div[2]")),"兑换")


    def tearDown(self):
        self.driver.quit()

if __name__ == "main":
    unittest.main()