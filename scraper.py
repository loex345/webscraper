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

def get_tag_data(driver, tag):
    """Get data for a specific tag from the page."""
    elements = driver.find_elements(By.TAG_NAME, tag)
    return [element.text for element in elements]

def autoscraper():
    link = input("Please input link: ")
    tags = input("Please input tags (separate multiple tags with commas, e.g., 'h1,p,div'): ").split(',')
    tags = [tag.strip() for tag in tags]  # Remove any whitespace
    
    driver = webdriver.Chrome()
    driver.get(link)
    
    # Dictionary to store data for each tag
    web_information = {}
    
    # Collect data for each tag
    for tag in tags:
        web_information[tag] = get_tag_data(driver, tag)
    
    driver.quit()
    
    # Create DataFrame with the longest list of data
    max_length = max(len(data) for data in web_information.values())
    df_dict = {}
    
    # Pad shorter lists with None to match the longest list
    for tag, data in web_information.items():
        df_dict[f"Tag_{tag}"] = data + [None] * (max_length - len(data))
    
    # Create DataFrame
    exportdata = pd.DataFrame(df_dict)
    
    # Print DataFrame
    print("\nScraped Data:")
    print(exportdata)
    
    # Export to Excel
    export_path = "/Users/mymac/downloads/results.xlsx"
    exportdata.to_excel(export_path, sheet_name="scraped_results", index=False)
    print(f"\nData exported to: {export_path}")

if __name__ == "__main__":
    autoscraper()