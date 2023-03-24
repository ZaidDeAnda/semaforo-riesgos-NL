from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import sys
import os

sys.path.append(f"{os.getcwd()}")
from noticias.utils.months import months

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# scraper

def find_articles(browser, keyword, date_start=None, date_end=None):
    if date_start and date_end:
        browser.get(f"https://news.google.com/search?q={keyword.replace(' ', '+')}%20after%3A{date_start}%20before%3A{date_end}")
    else:
        browser.get(f"https://news.google.com/search?q={keyword.replace(' ', '+')}%20when%3A7d")
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    return list(soup.find_all('article', class_='MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne'))

def extract_title(html):
    try:
        return html.find('a', class_='DY5T1d RZIKme').text
    except Exception as e:
        print(e)
        return None

def extract_url(html):
    try:
        url = html.find('a', class_='DY5T1d RZIKme')['href'][1:]
        return 'https://news.google.com'+url
    except Exception as e:
        print(e)
        return None

def extract_date(html):
    try:
        text = html.find('div', class_='QmrVtf RD0gLb kybdz').text
        text = text.replace('bookmark_bordersharemore_vert', '')
        return text
    except:
        return None

def change_date_format(date):
    new_date = date.split('-')[::-1]
    return '-'.join(new_date)

def get_date_time_ago(days):
    today_date = datetime.today()
    start_date = [str(today_date.year), str(today_date.month), str(today_date.day-days)]
    return '-'.join(start_date)

def add_weeks(week_number):
    date = '02-01-2023'
    date = datetime.datetime.strptime(date, '%d-%m-%Y')
    next_date = date + datetime.timedelta(days=7*(week_number-1))
    end_date = next_date + datetime.timedelta(days=6)
    next_date = datetime.datetime.strftime(next_date, '%d-%m-%Y')
    end_date = datetime.datetime.strftime(end_date, '%d-%m-%Y')
    return next_date, end_date

def format_week_column(week_number):
    start_date, end_date = add_weeks(week_number)
    start_date = start_date.split('-')
    end_date = end_date.split('-')
    return f"{start_date[0]} de {months[int(start_date[1])]} del {start_date[2]} al {end_date[0]} de {months[int(end_date[1])]}  del {end_date[2]}"

def scrap_news(date_start=None, date_end=None):

    if date_start:
        date_start = change_date_format(date_start)
    else:
        date_start = get_date_time_ago(7)

    if date_end:
        date_end = change_date_format(date_end)
    else:
        date_end = change_date_format(get_date_time_ago(0))

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome()

    # search

    data = []
    for key,values in keywords.items():
        

        df = pd.DataFrame()
        news = []
        for keyword in values:
            if date_end:
                news.extend(find_articles(browser, keyword, date_start, date_end))
            else:
                news.extend(find_articles(browser, keyword))
            
        df['html'] = news
        df['cat'] = key
        data.append(df)

    browser.close()
    data = pd.concat(data).reset_index(drop=True)

    data['title'] = data['html'].apply(extract_title)
    data['date'] = data['html'].apply(extract_date)
    print(datetime.datetime.strptime(date_start, '%Y-%m-%d').isocalendar()[1])
    data['week'] = datetime.datetime.strptime(date_start, '%Y-%m-%d').isocalendar()[1]
    data['url'] = data['html'].apply(extract_url)
    data['Periodo'] = data['week'].map(lambda x : format_week_column(int(x)))

    return data

# products

keywords = {
    'Nuevo León' : 
        [
            'Gobierno Nuevo León'
        ],
    'Igualdad' : 
        [
            'Inclusión Nuevo León',
            'Ruta Nuevo León',
            'Migrantes Nuevo León',
            'pobreza', 
            'Nuevo León'
        ],
    'Educación' : 
        [
            'Educación Nuevo León'
        ],
    'Samuel García' : 
        [
            'Samuel García Nuevo León'
        ]
    }