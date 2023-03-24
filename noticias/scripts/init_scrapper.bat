@echo off
set LOGFILE=batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

cd
call conda activate scrapping-env
cd C:\NL\semaforo-riesgos-nl\noticias

python "scrapper_init.py"