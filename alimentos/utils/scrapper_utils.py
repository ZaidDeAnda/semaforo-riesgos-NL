from bs4 import BeautifulSoup
import time
from os import path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .alimentos import url_dict

# scraper

def scrap_alimentos(fecha_1, fecha_2, browser):

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select

    #Establece la fecha
    fecha_inicio = Select(browser.find_element(By.ID, 'PeriodoInicio'))
    fecha_inicio.select_by_value(fecha_1)

    fecha_final = Select(browser.find_element(By.ID, 'PeriodoFin'))
    fecha_final.select_by_value(fecha_1)

    #Deselecciona ciudades
    browser.find_element(By.ID, 'SerieChBox-01').click()
    #Abre ciudades
    browser.find_element(By.ID, 'P01').click()
    #Selecciona ciudad de mexico
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[1]/tbody/tr[2]/td/div/table[3]/tbody/tr/td[1]/input').click()
    #Selecciona monterrey
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[1]/tbody/tr[2]/td/div/table[33]/tbody/tr/td[1]/input').click()


    #Abre Alimentos, bebidas y tabaco
    browser.find_element(By.ID, 'P001').click()
    #Abre alimentos
    browser.find_element(By.ID, 'P001011').click()

    ##### Inicia 1.1.1
    #Abre pan, tortillas y cereales
    browser.find_element(By.ID, 'P001011111').click()
    #Abre tortillas y derivados del maiz
    browser.find_element(By.ID, 'P001011111001').click()
    #Selecciona tostadas
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[1]/table[5]/tbody/tr/td[1]/input').click()
    #Selecciona Masa y harinas de maiz
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[1]/table[3]/tbody/tr/td[1]/input').click()
    #Selecciona maiz
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[1]/table[2]/tbody/tr/td[1]/input').click()
    #Abre Pan
    browser.find_element(By.ID, 'P001011111002').click()
    #Selecciona Pan dulce
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[2]/table[3]/tbody/tr/td[1]/input').click()
    #Selecciona pan de caja
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[2]/table[2]/tbody/tr/td[1]/input').click()
    #Abre galletas, pastas y harinas de trigo
    browser.find_element(By.ID, 'P001011111003').click()
    #Selecciona galletas
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[3]/table[1]/tbody/tr/td[1]/input').click()
    #Selecciona harinas de trigo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[3]/table[2]/tbody/tr/td[1]/input').click()
    #Selecciona pasta para sopa
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[3]/table[3]/tbody/tr/td[1]/input').click()
    #Abre Arroz y cereales preparados
    browser.find_element(By.ID, 'P001011111004').click()
    #Selecciona Arroz
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[1]/div[4]/table[1]/tbody/tr/td[1]/input').click()
    #### Aquí acaba 1.1.1

    #### Aquí inicia 1.1.2
    #Abre Carnes
    browser.find_element(By.ID, 'P001011112').click()
    #Abre Carne de ave
    browser.find_element(By.ID, 'P001011112005').click()
    #Selecciona pollo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/input').click()
    #Abre Carne y vísceras de cerdo
    browser.find_element(By.ID, 'P001011112006').click()
    #Selecciona carne de cerdo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[2]/div[2]/table[1]/tbody/tr/td[1]/input').click()
    #Abre carne y vísceras de res
    browser.find_element(By.ID, 'P001011112007').click()
    #Selecciona carne de res
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[2]/div[3]/table[1]/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.2

    #### Aquí inicia 1.1.3
    #Abre pescados y mariscos
    browser.find_element(By.ID, 'P001011113').click()
    # Abre pescados y mariscos
    browser.find_element(By.ID, 'P001011113009').click()
    # Selecciona pescado
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[3]/div[1]/table[3]/tbody/tr/td[1]/input').click()
    #Abre pescados y mariscos en conserva
    browser.find_element(By.ID, 'P001011113010').click()
    #Selecciona Atún y sardina en lata
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[3]/div[2]/table[1]/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.3

    #### Aquí inicia 1.1.4
    #Abre leche, derivados de leche y huevo
    browser.find_element(By.ID, 'P001011114').click()
    #Abre leche pasteurizada y fresca
    browser.find_element(By.ID, 'P001011114011').click()
    #Selecciona leche pasteurizada y fresca
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[4]/div[1]/table[2]/tbody/tr/td[1]/input').click()
    #Abre leche procesada
    browser.find_element(By.ID, 'P001011114012').click()
    #Selecciona leche en polvo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[4]/div[2]/table[1]/tbody/tr/td[1]/input').click()
    #Abre huevo
    browser.find_element(By.ID, 'P001011114014').click()
    #Selecciona huevo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[4]/div[4]/table/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.4

    #### Aquí inicia 1.1.5
    #Abre Aceites y grasas comestibles
    browser.find_element(By.ID, 'P001011115').click()
    #Abre Aceites y grasas vegetales comestibles
    browser.find_element(By.ID, 'P001011115015').click()
    #Selecciona Aceites y grasas vegetales comestibles
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[5]/div/table/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.5

    #### Aquí inicia 1.1.6
    #Abre Frutas y hortalizas
    browser.find_element(By.ID, 'P001011116').click()
    #Selecciona todas las frutas frescas
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[6]/table[1]/tbody/tr/td[2]/input').click()
    #Selecciona todas las hortalizas frescas
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[6]/table[2]/tbody/tr/td[2]/input').click()
    #Abre legumbres secas
    browser.find_element(By.ID, 'P001011116018').click()
    #Selecciona frijol
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[6]/div[3]/table[2]/tbody/tr/td[1]/input').click()
    #Abre frutas y legumbres procesadas
    browser.find_element(By.ID, 'P001011116019').click()
    #selecciona chiles envasados
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[6]/div[4]/table[2]/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.6

    #### Aquí inicia 1.1.7
    #Abre Azucar, cafe y refrescos envasados
    browser.find_element(By.ID, 'P001011117').click()
    #Abre azucar
    browser.find_element(By.ID, 'P001011117020').click()
    #selecciona azucar
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[7]/div[1]/table/tbody/tr/td[1]/input').click()
    #Abre cafe
    browser.find_element(By.ID, 'P001011117021').click()
    #Selecciona cafe soluble
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[7]/div[2]/table[1]/tbody/tr/td[1]/input').click()
    #Abre refrescos envasados y agua embotellada
    browser.find_element(By.ID, 'P001011117022').click()
    #Selecciona agua embotellada
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[7]/div[3]/table[1]/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.7

    #### Aquí inicia 1.1.8
    #Abre otros alimentos
    browser.find_element(By.ID, 'P001011118').click()
    #Abre chocolates y golosinas
    browser.find_element(By.ID, 'P001011118024').click()
    #Selecciona chocolate liquido y para preparar bebida
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[8]/div[2]/table[5]/tbody/tr/td[1]/input').click()
    #Selecciona gelatina en polvo
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/div/div/table[2]/tbody/tr[2]/td/div/div[1]/div[1]/div[8]/div[2]/table[4]/tbody/tr/td[1]/input').click()
    #### Aquí termina 1.1.8
    time.sleep(2)

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
