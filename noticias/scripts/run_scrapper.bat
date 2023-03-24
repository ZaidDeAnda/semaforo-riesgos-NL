@echo off
set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

conda activate scrapping-env

cd
call 
cd C:\NL\scrapper_noticias_nl\

cd ..
python "scrapper.py"