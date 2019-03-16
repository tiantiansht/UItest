# coding:utf-8
import time
import unittest
from selenium import webdriver
from common.Utils import Utils
from common.Judge import Judge
from selenium.webdriver.common.by import By
'''留言板页面测试'''
class testMessageBoard(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Utils = Utils(self.driver)
        self.Judge = Judge(self.driver)
        self.Utils.getUrl("http://wap.cmread.com/nap/p/zzzy_gdly.jsp?z=1&ln=1260_1337_3801_9_380_L3&mbid=S3dfgbNgqplvE4HCfil0MA%3D%3D&pageType=2&cm=M801005I&authorId=1000223695&type=0&vt=3&order=2&pageSize=6")

    def test_message_newest_top(self):
        '''留言板最新页面顶部测试'''
        self.Judge.is_text_in_element((By.XPATH,"//span[@class='co-font-larger co-bold']"),"留言板")
        self.Judge.is_presence_of_element((By.XPATH,"//span[@class='co-font-normal cmr-ar_title-num']"))
        self.assertEqual(self.Utils.getText((By.CSS_SELECTOR,"a.co-font-big.cmr-ar_title-hot")),"最热")
        self.assertEqual(self.Utils.getText((By.XPATH,"//a[@class='co-font-big cmr-ar_title-new active']")),"最新")

    def test_message_newest_comment(self):
        '''留言板最新页评论区'''
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/a/img[1]"),"src"))
        self.Utils.click((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/a"))
        self.Judge.is_title("TA的主页")
        self.driver.back()
        time.sleep(3)
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/div/div/a"),"href"))
        self.Utils.click((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/div/div/a"))
        self.driver.back()
        time.sleep(3)
        self.Judge.isfindElement((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/a/span[2][@class='cmr-break']"))
        self.Judge.is_presence_of_element((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/div /span[@class='co-font-normal cmr-ar-msgCon-time']"))
        self.Judge.is_presence_of_element((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/div /span[@class='cmr-ar-msgCon-thumbs']/span[1]"))
        self.Judge.is_presence_of_element((By.XPATH,"//section[@class='cmr-ar-msg']/div[1]/div/div /span[@class='cmr-ar-msgCon-thumbs']/span[2]"))

    def test_message_newest_drop_down(self):
        '''留言板最新下拉底部测试'''
        self.Utils.js_scroll_end()
        self.Judge.isfindElement((By.CSS_SELECTOR,"span.pagger-finish-text"))
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH,"//section[@class='cmr-ar-msg']/div[last()]/a/img"),"src"))
        self.Utils.click((By.XPATH,"//section[@class='cmr-ar-msg']/div[last()]/a"))
        self.Judge.is_title("TA的主页")
        self.driver.back()
        time.sleep(3)
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/div/a"), "href"))
        self.Utils.click((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/div/a"))
        self.driver.back()
        time.sleep(3)
        self.Judge.isfindElement((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/a/span[2]"))
        self.Judge.is_presence_of_element((By.XPATH,"//section[@class='cmr-ar-msg']/div[last()]/div/div/span"))
        self.Judge.is_presence_of_element((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/span[2]/span[1]"))
        self.Judge.is_presence_of_element((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/span[2]/span[2]"))

    def test_message_hottest(self):
        '''留言板最热页面测试'''
        self.Utils.click((By.CSS_SELECTOR, "a.co-font-big.cmr-ar_title-hot"))
        self.Utils.js_scroll_end()
        self.Judge.isfindElement((By.CSS_SELECTOR, "span.pagger-finish-text"))
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/a/img"), "src"))
        self.Utils.click((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()-2]/a"))
        self.Judge.is_title("TA的主页")
        self.driver.back()
        time.sleep(3)
        self.assertIsNotNone(self.Utils.get_Url((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/div/a"), "href"))
        self.Judge.isfindElement((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/div/a"))
        self.Judge.isfindElement((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/a/span[2]"))
        self.Judge.is_presence_of_element((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/span"))
        self.Judge.is_presence_of_element((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/span[2]/span[1]"))
        self.Judge.is_presence_of_element((By.XPATH, "//section[@class='cmr-ar-msg']/div[last()]/div/div/span[2]/span[2]"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

