import os
import pandas as pd
import datetime

from utils.scrapper_utils import scrap_news

today_date = datetime.datetime.now()
today_date_str = datetime.datetime.strftime(today_date, '%d-%m-%Y')
week_ago_date = today_date - datetime.timedelta(days=7)
week_ago_date_str = datetime.datetime.strftime(week_ago_date, '%d-%m-%Y')

data = scrap_news(week_ago_date_str, today_date_str).drop('html',axis=1)

if os.path.exists(r'noticias/data/Noticias.csv'):
    df = pd.read_csv(r'noticias/data/Noticias.csv')
    data = pd.concat([df,data])
    
data.to_csv(r'noticias/data/Noticias.csv',index = False)