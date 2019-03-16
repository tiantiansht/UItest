# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Utils():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.interval = 0.5

    def findElement(self,loctor):
        '''使用显性等待发现元素'''
        ele = WebDriverWait(self.driver,self.timeout,self.interval).until(lambda x: x.find_element(*loctor))
        return ele

    def findElements(self,loctor):
        '''使用显性等待发现元素组'''
        ele = WebDriverWait(self.driver,self.timeout,self.interval).until(lambda x: x.find_elements(*loctor))
        return ele

    def click(self,loctor):
        '''元素点击'''
        ele = self.findElement(loctor)
        ele.click()

    def sendKeys(self, loctor, text):
        '''输入文本'''
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def clear(self, loctor):
        '''清空'''
        ele = self.findElement(loctor)
        ele.clear()

    def submit(self, loctor):
        '''表单提交点击'''
        ele = self.findElement(loctor)
        ele.submit()

    def run_js(self,js):
        '''执行js'''
        self.driver.execute_script(js)


    def js_scroll_top(self):
        '''页面滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.run_js(js)

    def js_scroll_end(self):
        '''页面滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.run_js(js)


    def js_focus_element(self,locator):
        '''定位元素滚动页面位置'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def get_Url(self,loctor,value):
        '''获取元素值'''
        ele = self.findElement(loctor).get_attribute(value)
        return ele

    def getText(self,loctor):
        '''获取文本'''
        ele = self.findElement(loctor).text
        return ele

    def getUrl(self,url):
        '''访问网站'''
        self.driver.get(url)

    def lazyLoading_scroll_end(self):
        '''懒加载页面滑动至底部'''
        all_window_height = []
        all_window_height.append(self.driver.execute_script("return document.body.scrollHeight;"))
        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            check_height = self.driver.execute_script("return document.body.scrollHeight;")
            if check_height == all_window_height[-1]:
                break
            else:
                all_window_height.append(check_height)



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://wap.cmread.com/nap/p/mgyjply_new.jsp")
    ele = driver.find_element_by_css_selector("div>a.cmr-more-url.co-font-big>span")
    ele.click()




