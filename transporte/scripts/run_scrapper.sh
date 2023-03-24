# Run python script
python transporte/scripts/scrapper.py

cp $PWD'/transporte/data/INP_PP_CAB18.csv' 'transporte/data/Inegi_inflacion_last_year.csv'
cp $PWD'/transporte/data/INP_PP_CAB18 (1).csv' 'transporte/data/Inegi_inflacion_current_year.csv'

rm $PWD'/transporte/data/INP_PP_CAB18.csv'
rm $PWD'/transporte/data/INP_PP_CAB18 (1).csv'