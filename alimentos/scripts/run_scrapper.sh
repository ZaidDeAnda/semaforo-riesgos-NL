# Run python script
python alimentos/scripts/scrapper.py

cp $PWD'/alimentos/data/INP_PP_CAB18.csv' 'alimentos/data/Inegi_inflacion_last_year.csv'
cp $PWD'/alimentos/data/INP_PP_CAB18 (1).csv' 'alimentos/data/Inegi_inflacion_current_year.csv'

rm $PWD'/alimentos/data/INP_PP_CAB18.csv'
rm $PWD'/alimentos/data/INP_PP_CAB18 (1).csv'