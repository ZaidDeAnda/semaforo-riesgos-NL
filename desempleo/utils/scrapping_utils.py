from zipfile import ZipFile

def extract_trimestral_files():
    for i in range(1,5):
        try:
            with ZipFile(f"desempleo/data/{i}_2022.zip", 'r') as zip:
                zip.extract(f'Ciudades/2022_trim_{i}_Cd_Monterrey.xls', path='desempleo/data')
        except Exception as e:
            print(e)