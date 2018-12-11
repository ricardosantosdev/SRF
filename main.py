# coding: utf-8

from src.srf import *
import sys

if len(sys.argv) == 3:
    browser(sys.argv[1])
    print('\033[32m' + "Diretório atual: ", current_directory() + '\033[0;0m')
    print("-----------------------------------------------------------")
    to_cleaner(sys.argv[2])
else:
    print('ERROR: Waiting arguments...')

