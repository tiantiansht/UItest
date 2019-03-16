# coding:utf-8
from selenium import webdriver
from common.Utils import Utils
from common.Judge import Judge
from selenium.webdriver.common.by import By
class candao():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.Utils = Utils(self.driver)
        self.Judge = Judge(self.driver)

    def candao_page_element(self,username,password):
        self.Utils.sendKeys((By.CSS_SELECTOR,"[name='account']"),username)
        self.Utils.sendKeys((By.CSS_SELECTOR,"[name='password']"),password)
        self.Utils.click((By.XPATH,"//button[@id='submit']"))
        try:
            result = self.driver.find_element_by_xpath("//div[@class='pull-right']/a[1]").text
            return result
        except:
            result = "无退出"
            return result

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    candao = candao(driver,'admin','123456')
    candao.candao_page_element()
