from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from urllib.parse import urlencode
import json
import httpx

#Go through API 
BASE_HEADERS = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US;en;q=0.9",
    "accept-encoding": "gzip, deflate, br"
}
url ="https://www.zillow.com/search/GetSearchPageState.htm?"
#Set Query information
parameters = {
    "searchQueryState": {
        "pagination": {},
        "usersSearchTerm": "New Haven, CT",
        # map coordinates that indicate New Haven city's area
        "mapBounds": {
            "west": -73.03037621240235,
            "east": -72.82781578759766,
            "south": 41.23043771298298,
            "north": 41.36611033618769,
        },
    },
    "wants": {
        # cat1 stands for agent listings
        "cat1": ["mapResults"]
        # and cat2 for non-agent listings
        # "cat2":["mapResults"]
    },
    "requestId": 2,
}
def autoscraper():
    response = httpx.get(url + urlencode(parameters), headers=BASE_HEADERS)
    data = response.json()
    results = response.json()["cat1"]["searchResults"]["mapResults"]
    print(json.dumps(results, indent=2))
    print(f"found {len(results)} property results")

autoscraper()


# follow this guide https://scrapfly.io/blog/how-to-scrape-zillow/
#Create web place 

# def autoscraper():
#     driver = webdriver.Chrome()

#     driver.get("https://scrapfly.io/blog/how-to-scrape-zillow/")

#     content = driver.page_source
#     title = driver.title

#     divs = driver.find_element(By.TAG_NAME,"script")

#     for d in divs:
#         print(d.text)
# autoscraper()