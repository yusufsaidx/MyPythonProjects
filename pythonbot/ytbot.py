from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
link = input('link girin')
driver = webdriver.Chrome("C:/Users/syusu/Desktop/chromedriver.exe")
for a in range(10):
    for i in range(15):
        driver.get(link)
        print(i)
        time.sleep(2)
        
