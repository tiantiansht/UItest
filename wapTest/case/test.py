# coding:utf-8
import unittest
import time
from common.Utils import Utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.Judge import Judge
driver = webdriver.Chrome()
Utils = Utils(driver)
driver.get("http://wap.cmread.com/nap/p/exchange_store.jsp")
ele = Utils.getText((By.XPATH,"//ul[@class='cmr-bookticket_exchange-lists']/li[1]/div[1]/p[1]"))
print(ele)
