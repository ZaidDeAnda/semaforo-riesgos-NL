@echo off
set YEAR=2022
set TRIM=4

echo Ejecutando scrapper del tabulado

del desempleo\data\Tabulado.csv

python desempleo\scripts\scrapper.py

echo Bajando los indicadores por ciudad para %YEAR% trimestre %TRIM%

curl "https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/tabulados/enoe_n_indicadores_estrategicos_%YEAR%_trim%TRIM%_xls.zip" --output "desempleo\data\%TRIM%_%YEAR%.zip"

echo Extrayendo los archivos de los zips

python desempleo\scripts\preprocess.py

echo Acomodando los indicadores por ciudad para %YEAR% trimestre %TRIM%

move "desempleo\data\Ciudades\%YEAR%_trim_%TRIM%_Cd_Monterrey.xls" "desempleo\data\%YEAR%_trim_%TRIM%_Cd_Monterrey.xls" 
del "desempleo\data\%TRIM%_%YEAR%.zip"

rmdir desempleo\data\Ciudades

echo Limpiando los datos

python desempleo\scripts\process.py
