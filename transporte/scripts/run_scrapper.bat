@echo off
set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

cd
call conda activate scrapping-env
cd C:\NL\scrapper_transporte_nl\

cd ..
python "scrapper.py"
cd data

copy "INP_PP_CAB18.csv" "Inegi_inflacion_last_year.csv"
copy "INP_PP_CAB18 (1).csv" "Inegi_inflacion_current_year.csv"

del "INP_PP_CAB18.csv"
del "INP_PP_CAB18 (1).csv"