import sys
import os

sys.path.append(f"{os.getcwd()}")

print(sys.path)

from desempleo.utils.scrapping_utils import extract_trimestral_files

extract_trimestral_files()