from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.parse import urlencode
from openpyxl import Workbook
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

    data = driver.find_elements(By.TAG_NAME,linktag)

    #print(f'Content {divs}')

    x = type(data)
    print(x)

    #for d in data:
        #print(d.text) 
    driver.quit()
    #Add Data (list) to dataframe
    #Unpack data from from selenium through loop 
    #Send that data to the data frame
    # Reorganize code
    exportdata = pd.DataFrame(data,columns=["Tag"])
    #Print Data frame
    print(exportdata)
    exportdata.to_excel("/Users/mymac/downloads/results.xlsx", sheet_name="sheetone")

autoscraper()