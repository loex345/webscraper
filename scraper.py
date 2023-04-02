from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd


def autoscraper():
    driver = webdriver.Chrome()

    driver.get("https://scrapfly.io/blog/how-to-scrape-zillow/")

    content = driver.page_source
    title = driver.title

    divs = driver.find_element(By.TAG_NAME,"script")

    for d in divs:
        print(d.text)
autoscraper()