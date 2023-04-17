from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.parse import urlencode

# follow this guide https://scrapfly.io/blog/how-to-scrape-zillow/
#Create web place 

def autoscraper():
    driver = webdriver.Chrome()

    driver.get('https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-85.20889236975107%2C%22east%22%3A-84.77493240881357%2C%22south%22%3A34.917369310071535%2C%22north%22%3A35.25617591697837%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3002%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D')

    content = driver.page_source
    title = driver.title

    divs = driver.find_elements(By.TAG_NAME,"div")

    for d in divs:
        print(d.text) 
autoscraper()