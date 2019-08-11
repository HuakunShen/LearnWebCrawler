import time
from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
time.sleep(1)
browser.get('https://www.google.ca/')
time.sleep(1)
browser.get('https://www.python.org/')
time.sleep(1)
browser.back()
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.close()