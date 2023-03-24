echo "Ejecutando scrapper del tabulado"

rm desempleo/data/Tabulado.csv

python desempleo/scripts/scrapper.py

echo "Bajando los indicadores por ciudad"

curl https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/tabulados/enoe_n_indicadores_estrategicos_2022_trim4_xls.zip --output desempleo/data/4_2022.zip

echo "Extrayendo los archivos de los zips"

python desempleo/scripts/preprocess.py

echo "Acomodando los indicadores por ciudad"

    mv desempleo/data/Ciudades/2022_trim_4_Cd_Monterrey.xls desempleo/data/2022_trim_4_Cd_Monterrey.xls 
    rm desempleo/data/4_2022.zip

rmdir desempleo/data/Ciudades

echo "Limpiando los datos"

python desempleo/scripts/process.py

