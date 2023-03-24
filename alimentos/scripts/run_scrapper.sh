# Run python script
python scrapper.py

cp $PWD'/alimentos/data/INP_PP_CAB18.csv' 'data/Inegi_inflacion_last_year.csv'
cp $PWD'/alimentos/data/INP_PP_CAB18 (1).csv' 'data/Inegi_inflacion_current_year.csv'

rm $PWD'/alimentos/data/INP_PP_CAB18.csv'
rm $PWD'/alimentos/data/INP_PP_CAB18 (1).csv'