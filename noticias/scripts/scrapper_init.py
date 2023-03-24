import os
import pandas as pd
import sys

sys.path.append(f"{os.getcwd()}")

from noticias.utils.scrapper_utils import scrap_news

#Hay que automatizar esto

dates = {
    '02-01-2023' : '08-01-2023',
    '09-01-2023' : '15-01-2023',
    '16-01-2023' : '22-01-2023',
    '23-01-2023' : '29-01-2023',
    '30-01-2023' : '05-02-2023',
    '06-02-2023' : '12-02-2023',
    '13-02-2023' : '19-02-2023',
    '20-02-2023' : '26-02-2023',
    '27-02-2023' : '05-03-2023',
    '06-03-2023' : '12-03-2023'
}

for date in dates.items():    
    data = scrap_news(date[0], date[1]).drop('html',axis=1)

    if os.path.exists(r'noticias/data/Noticias.csv'):
        df = pd.read_csv(r'noticias/data/Noticias.csv')
        data = pd.concat([df,data])
        
    data.to_csv(r'noticias/data/Noticias.csv',index = False)