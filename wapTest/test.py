from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\邵航天\AppData\Local\Google\Chrome\User Data\Default")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com")
driver.quit()

