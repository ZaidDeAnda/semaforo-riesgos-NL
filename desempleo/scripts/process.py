import sys
import os

sys.path.append(f"{os.getcwd()}")

from desempleo.utils.data_utils import read_trimestral_data

read_trimestral_data("desempleo/data/2022_trim_4_Cd_Monterrey.xls")