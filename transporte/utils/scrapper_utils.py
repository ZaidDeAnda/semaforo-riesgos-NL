from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# scraper

def scrap_alimentos(fecha_1, fecha_2, browser):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select

    #Establece la fecha
    fecha_inicio = Select(browser.find_element(By.ID, 'PeriodoInicio'))
    fecha_inicio.select_by_value(fecha_1)
    time.sleep(1)

    fecha_final = Select(browser.find_element(By.ID, 'PeriodoFin'))
    fecha_final.select_by_value(fecha_1)
    time.sleep(1)

    #Deselecciona ciudades
    browser.find_element(By.ID, 'SerieChBox-01').click()
    time.sleep(1)
    #Abre ciudades
    browser.find_element(By.ID, 'P01').click()
    time.sleep(1)
    #Selecciona ciudad de mexico
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[1]/tbody/tr[2]/td/div/table[3]/tbody/tr/td[1]/input').click()
    time.sleep(1)
    #Selecciona monterrey
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[1]/tbody/tr[2]/td/div/table[33]/tbody/tr/td[1]/input').click()
    time.sleep(1)

    #### Transporte

    # Abre 6 transporte
    browser.find_element(By.ID, 'P006').click()
    time.sleep(1)
    # Selecciona 6.1 transporte publico
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[6]/table[1]/tbody/tr/td[2]/input').click()
    time.sleep(1)

    #### Guarda el csv
    l = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div[2]/a[4]')
    browser.execute_script("arguments[0].click();", l);
    print("Descargando csv 1")
    time.sleep(4)

    #Establece la segunda fecha
    fecha_inicio = Select(browser.find_element(By.ID, 'PeriodoInicio'))
    fecha_inicio.select_by_value(fecha_2)
    time.sleep(1)

    fecha_final = Select(browser.find_element(By.ID, 'PeriodoFin'))
    fecha_final.select_by_value(fecha_2)
    time.sleep(1)

    #### Guarda el csv
    l = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div[2]/a[4]')
    browser.execute_script("arguments[0].click();", l);
    print("Descargando csv 2")
    time.sleep(4)
