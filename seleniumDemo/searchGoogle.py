from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://www.google.ca')
input = browser.find_element_by_xpath('//*[@class="gLFyf gsfi"]')
input.send_keys('selenium')
time.sleep(1)
input.send_keys(Keys.ENTER)
# browser.close()