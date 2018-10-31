# coding: utf-8

from src.srf import *

browser(input("Navegue para o diretório onde deseja executar a limpeza:\n>> "))
print('\033[32m'+"Diretório atual: ", current_directory()+'\033[0;0m')
to_cleaner(input("Defina quais arquivos deseja remover filtrando por caracteres:\n>> "))
