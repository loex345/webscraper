from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.parse import urlencode
#import numpy as np
# follow this guide https://scrapfly.io/blog/how-to-scrape-zillow/
#Create web place 
titles=[]
def autoscraper():
    link = input("Please input link")
    linktag = input("Please input tag")
    driver = webdriver.Chrome()
    results = requests.get(link)
    url = driver.get(link)
    
    content = driver.page_source
    title = driver.title

    divs = driver.find_elements(By.TAG_NAME,linktag)

    #print(f'Content {divs}')

    for d in divs:
        print(d.text) 
    driver.quit()
autoscraper()