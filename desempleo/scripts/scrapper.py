import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

current_path = f"{os.getcwd()}/desempleo/data"

chrome_options = Options()
chrome_options.add_argument("--incognito")
prefs = {
    'download.default_directory' : current_path,
    'profile.default_content_setting_values.automatic_downloads': 1
    }
chrome_options.add_experimental_option('prefs', prefs)
browser= webdriver.Chrome(chrome_options=chrome_options)

browser.get("https://www.inegi.org.mx/app/tabulados/default.html?nc=625&idrt=18&opc=t")
time.sleep(1)

csv_button = browser.find_element(By.ID, 'aCsv')
browser.execute_script("arguments[0].click();", csv_button);
print("Descargando csv")
time.sleep(4)

browser.close()






