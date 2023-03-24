import pandas as pd
import datetime
import os

from .alimentos import url_dict

food_groups = {
    'Frutas frescas' : '16 Frutas frescas',
    'Hortalizas frescas' : '17 Hortalizas frescas'
}

def clean_title(title_string):
    title_string = title_string.replace(',', '')
    title_list = title_string.split(' ')
    try:
        index = title_list.index('ciudad')
        end_index = title_list[index+1:].index('Por')
        return(' '.join(title_list[index+1:index+1+end_index])) 
    except:
        return "Resumen nacional"
    
def calculate_percentage(df):
    wanted_columns = df.columns.tolist()[12:]
    for date in wanted_columns[::-1]:
        previous_date = date.split(' ')[0] + ' ' + str(int(date.split(' ')[1])-1)
        df[date] = (df[date]/df[previous_date] - 1) * 100
    return df[wanted_columns]

def read_historical():
    df = pd.read_excel('alimentos/data/ca61_2018.xlsx', header=4, index_col='Título')
    df = df.iloc[8:-4]
    new_names_dict = {col : clean_title(col) for col in df.columns.tolist()}
    df.rename(columns=new_names_dict, inplace=True)
    df = df.T
    df = calculate_percentage(df)
    return df

def substitute_group_with_mean(df, food):
    food_code = food_groups[food]
    promedio = df.loc[df['Subclase'] == food_code]['Precio promedio'].mean()
    df.loc[df['Subclase'] == food_code, ['Genérico', 'Precio promedio']] = [food, promedio]
    return df

def load_inegi_df(path : str):
    df = pd.read_csv(path, header=4, encoding='latin')
    df['Unidad'] = df['Unidad'].str.replace(' ', '')
    if df["Fecha_Pub_DOF"].isnull().values.any():
        df["Fecha_Pub_DOF"] = datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y')
    df = df.loc[(df['Unidad'] == "KG") | (df['Unidad'] == "LT") | (df['Unidad'] == "VIAJE") | (df['Unidad'] == "BOLETO") | (df['Unidad'] == "SERV")]
    for food in food_groups.keys():
        df = substitute_group_with_mean(df, food)
    return df

def get_mean_df(df_last, df_current):
    df_kg = pd.concat([df_last, df_current])
    df_mean = df_kg[['Precio promedio','Genérico', 'Nombre ciudad', 'Año']].groupby(['Año', 'Nombre ciudad', 'Genérico']).mean()
    df_mean = df_mean.reset_index(level = ('Año'))
    return df_mean

def separate_df(df, current_year, last_year):
    df_separated = df.loc[df['Año'] == last_year]
    df_separated.rename(columns={'Precio promedio' : f'Precio promedio {last_year}'}, inplace=True)
    df_separated = df_separated.drop('Año', axis=1)
    df_separated[f'Precio promedio {current_year}'] = df.loc[df['Año'] == current_year]['Precio promedio']
    return df_separated

def add_url_to_top_dict(top_dict):
    for key in top_dict.keys():
        ratio = top_dict[key]
        top_dict[key] = {
            'ratio' : ratio,
            'url' : url_dict[key]
        }
    return top_dict

def calculate_ratio(category):
    df_last = load_inegi_df(f'{category}/data/Inegi_inflacion_last_year.csv')
    df_current = load_inegi_df(f'{category}/data/Inegi_inflacion_current_year.csv')
    df_mean = get_mean_df(df_last, df_current)
    comparison_month = df_last.iloc[0]['Mes']
    current_year = df_current.iloc[0]['Año']
    last_year = int(current_year)-1
    df_separated = separate_df(df_mean, current_year, last_year)
    df_separated['ratio'] = ((df_separated[f'Precio promedio {current_year}']/df_separated[f'Precio promedio {last_year}']) - 1) * 100
    df_separated = df_separated.reset_index(level='Nombre ciudad')
    df_ordered = df_separated.sort_values('ratio', ascending=False)
    top_6_items = df_ordered.loc[df_ordered['Nombre ciudad'] == 'Monterrey, N.L.'].head(6)['ratio'].to_dict()
    if category == "alimentos":
        top_6_items = add_url_to_top_dict(top_6_items)
    return df_ordered, comparison_month, top_6_items