import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from utils.scrapper_utils import scrap_alimentos

current_path = f"{os.getcwd()}/alimentos/data"
print(current_path)

chrome_options = Options()
chrome_options.add_argument("--incognito")
prefs = {
    'download.default_directory' : current_path,
    'profile.default_content_setting_values.automatic_downloads': 1
    }
chrome_options.add_experimental_option('prefs', prefs)
browser= webdriver.Chrome(chrome_options=chrome_options)

browser.get("https://www.inegi.org.mx/app/preciospromedio/?bs=18")
time.sleep(1)
soup = BeautifulSoup(browser.page_source,'html.parser')

today = datetime.datetime.now()
one_month_ago = today - datetime.timedelta(days=45)
lastMonth = one_month_ago.month
lastMonth = f"0{lastMonth}" if lastMonth < 10 else str(lastMonth)
year = one_month_ago.year

print(f"Se scrappearan datos desde {year-1}{lastMonth} hasta {year}{lastMonth}")

scrap_alimentos(browser=browser, fecha_1=f"{year-1}{lastMonth}", fecha_2=f"{year}{lastMonth}")