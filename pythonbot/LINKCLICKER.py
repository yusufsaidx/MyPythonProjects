from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
link = input('input link...')
driver = webdriver.Chrome("your file path "CHROME WEB DRIVER")
for a in range(10):
    for i in range(15):
        driver.get(link)
        print(i)
        time.sleep(2)
