import pandas as pd

new_columns = [
    "Year",
    "Period",
    "L1",
    "L2",
    "L3",
    "L4",
    "Total",
    "Coeficiente de variacion",
    "Error estandar",
    "LIIC",
    "LSIC"
]

def add_level_to_category(df, category_name):
    flag = False

    subcategory = " "
    for row in df.loc[df['Unnamed: 0'] == category_name].iterrows():
        if row[1]['Unnamed: 1'][0].isnumeric():
            flag = True
            if row[1]['Unnamed: 1'] != subcategory:
                subcategory = row[1]['Unnamed: 1']
                continue
        if flag == True:
            row[1]['L4'] = row[1]['Unnamed: 2']
            row[1]['Unnamed: 2'] = row[1]['Unnamed: 1']
            row[1]['Unnamed: 1'] = subcategory
        df.loc[row[0]] = row[1]
    
    return df

def read_trimestral_data(filename):

    file = filename.split("/")[2]
    year, period = file.split("_")[0], file.split("_")[2]

    df = pd.read_excel(filename, header=7).iloc[:286]
    df = df.drop('Unnamed: 3', axis=1)

    df = df.dropna(how="all")

    df.insert(3, 'L4', " ")

    for level in range(2):
        new_col = []
        temp_title = " "
        for row in df.iterrows():
            if type(row[1][level]) is str:
                temp_title = row[1][level]
            new_col.append(temp_title)
        df[f"Unnamed: {level}"] = new_col

    df = add_level_to_category(df, '3. Población ocupada por:')
    df = add_level_to_category(df, '7. Población desocupada por:')

    df.insert(0, "Year", year)
    df.insert(1, "Period", period)

    clean_df = df.drop(['Total', 'Total.1', 'Total.2', 'LIIC', 'LSIC'], axis=1)
    
    duplicated_df = pd.concat([clean_df]*2).sort_index().reset_index(drop=True)

    hombres = duplicated_df.columns.tolist()[6::2]
    mujeres = duplicated_df.columns.tolist()[7::2]
    sex_list = []
    for row in duplicated_df.iterrows():
        if row[0]%2 == 1:
            for columna_hombres, columna_mujeres in zip(hombres, mujeres):
                row[1][columna_hombres] = row[1][columna_mujeres]
            sex_list.append("Mujer")
        else:
            sex_list.append("Hombre")
        duplicated_df.loc[row[0]] = row[1]

    duplicated_df = duplicated_df.drop(mujeres, axis=1)
    duplicated_df.columns = new_columns
    duplicated_df.insert(2, "Sexo", sex_list)

    duplicated_df.to_csv("desempleo/data/descomposicion.csv")

def read_tabulado():
    
    with open("desempleo/data/Tabulado.csv", encoding="utf-8") as f:
        data = f.readlines()

    data = [line[:-1] for line in data]

    data[0] = data[0][1:]
    header = data[0].split(",")[1:]
    data = data[1:-2]

    new_data = []
    indexes = []
    for block in data:
        if block[0] == "2":
            year = block
            continue
        block_list = block.split(",")
        indexes.append(year +" "+ block_list[0])
        block_list = block_list[1:]
        block_list = [float(x) for x in block_list]
        new_data.append(block_list)

    tabulado_df = pd.DataFrame(data=new_data, columns=header, index=indexes).T

    tabulado_df.loc['Media'] = tabulado_df.describe().loc['mean']

    return tabulado_df