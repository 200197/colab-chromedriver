!pip install selenium
!apt-get update 
!apt install chromium-chromedriver

import selenium
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from tqdm import tqdm

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wbD = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

print("============================================================")
wbD.get('https://www.ikea.com.hk/en/products/sofas-and-armchairs/sofas')
price = wbD.find_element_by_xpath('//*[@id="card_30245044"]/div[2]/div[1]/div[3]/div/p').text
print(price)
