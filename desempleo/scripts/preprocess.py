import sys
import os

sys.path.append(f"{os.getcwd()}")

from desempleo.utils.scrapping_utils import extract_trimestral_files

extract_trimestral_files()