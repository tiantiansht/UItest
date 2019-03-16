# coding:utf-8
import time
import unittest
from selenium import webdriver
from common.Utils import Utils
from common.Judge import Judge
from selenium.webdriver.common.by import By
class testRewardList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Utils = Utils(self.driver)
        self.Judge = Judge(self.driver)
        self.Utils.getUrl("http://wap.cmread.com/nap/p/ds_rank.jsp?z=1&ln=2403_2407_3801_1_380_L1&cm=M801005I&vt=3")

    def test_reward_book(self):
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//img[@class='tae-img lazy-really-loaded lazy-loaded']"),"src"))
        self.assertEqual(self.Utils.getText((By.XPATH,"//span[@class='co-bold cmr-rank_tab-topOne']")),"TOP.1")
        self.assertEqual(self.Utils.getText((By.XPATH,"//div[@class='cmr-rank_list']/a[1]/aside/p/span[2]")),"惜花芷")
        self.Judge.is_presence_of_element((By.XPATH,"//div[@class='cmr-rank_list']/a[1]/aside/p[2]/i"))
        self.Judge.is_presence_of_element((By.XPATH,"//div[@class='cmr-rank_list']/a[1]/aside/p[2]/span"))
        self.Utils.click((By.XPATH,"//div[@class='cmr-rank_list']/a[1]"))
        self.Judge.is_title("图书详情")

    def test_reward_drop_down(self):
        self.Utils.lazyLoading_scroll_end()
        self.assertEqual(self.Utils.getText((By.CSS_SELECTOR,"div.pagger-finish-box>span")),"已显示全部")
        self.assertEqual(self.Utils.getText((By.XPATH, "//div[@class='cmr-rank_list']/a[last()]/aside/p/span")),"100.")
        self.Judge.is_presence_of_element((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]/aside/p/span[2]"))
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]/figure/img"),"src"))
        self.Judge.is_presence_of_element((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]/aside/p[2]/i"))
        self.Judge.isfindElement((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]/aside/p[2]/span"))
        self.Judge.isfindElement((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]/aside/p[3]"))
        self.Utils.click((By.XPATH,"//div[@class='cmr-rank_list']/a[last()]"))
        self.Judge.is_title("图书详情")

    def tearDown(self):
        self.driver.quit()

if __name__ == "main":
    unittest.main()