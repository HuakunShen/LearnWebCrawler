import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
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