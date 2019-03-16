# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Judge():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.interval = 0.5

    def is_title(self,text):
        '''判断页面标题是否等于预期值'''
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.interval).until(EC.title_is(text))
            return ele
        except:
            return False

    def isfindElement(self,loctor):
        '''判断元素是否存在'''
        try:
            WebDriverWait(self.driver, self.timeout, self.interval).until(lambda x: x.find_element(*loctor))
            return True
        except:
            return False

    def is_presence_of_element(self,loctor):
        '''判断元素是否在dom树'''
        try:
            WebDriverWait(self.driver,self.timeout,self.interval).until(EC.presence_of_element_located(loctor))
            return True
        except:
            return False

    def is_visibility_of_element(self,loctor):
        '''判断元素是否可见，可见非隐藏'''
        try:
            WebDriverWait(self.driver,self.timeout,self.interval).until(EC.visibility_of_element_located(loctor))
            return True
        except:
            return False

    def is_text_in_element(self,loctor,text):
        '''判断元素中的text是否包含预期值'''
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.interval).until(EC.text_to_be_present_in_element(loctor,text))
            return ele
        except:
            return False

    def is_element_value(self,loctor,text):
        '''判断某个元素的value值是否包含了预期结果'''
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.interval).until(EC.text_to_be_present_in_element_value(loctor,text))
            return ele
        except:
            return False

    def is_element_click(self,loctor):
        '''判断元素是否能点击或输入'''
        try:
            WebDriverWait(self.driver,self.timeout,self.interval).until(EC.element_to_be_clickable(loctor))
            return True
        except:
            return False


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    judge = Judge(driver)
    ele = judge.is_element_click((By.ID,"kw"))
    print(ele)