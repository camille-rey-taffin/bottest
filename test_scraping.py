import json


# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

options = Options()
options.headless = True
# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(options=options, executable_path = './chromedriver')

# get web page
driver.get('https://devdocs.io/settings')
time.sleep(1)

driver.find_elements_by_xpath("//*[@id='settings']/div/div/div[contains(@class,'icon-python')]")[0].click()
time.sleep(1)
driver.find_elements_by_xpath("/html/body//input[@type='checkbox' and @name='python~3.9']")[0].click()


time.sleep(1)

driver.find_elements_by_xpath("//button[@type='submit']")[0].click()


time.sleep(1)

driver.get('https://devdocs.io/#q=python%20rstrip')
time.sleep(2)
#results = driver.find_elements_by_xpath("//a")
# execute script to scroll down the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
#sleep for 30s
time.sleep(2)
results = driver.find_elements_by_xpath("//a")

for lien in results:
    print(lien.get_attribute("href"))
print('Number of results', len(results))

driver.quit()
