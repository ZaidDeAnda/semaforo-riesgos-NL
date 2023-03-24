# Run python script
python scrapper.py

cp $PWD'/transporte/data/INP_PP_CAB18.csv' 'data/Inegi_inflacion_last_year.csv'
cp $PWD'/transporte/data/INP_PP_CAB18 (1).csv' 'data/Inegi_inflacion_current_year.csv'

rm $PWD'/transporte/data/INP_PP_CAB18.csv'
cp $PWD'/transporte/data/INP_PP_CAB18 (1).csv'