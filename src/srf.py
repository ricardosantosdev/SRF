# coding: utf-8

import os
import glob


def current_directory():
    """
    :return: Mostra na tela o diretório atual.
    """
    return os.getcwd()


def navigator(direct):
    """
    :param direct:
    :return: Seta o diretório inserido pelo usuário.
    """
    return os.chdir(direct)


def to_cleaner(filtering):
    """
    :param filtering:
    :return: Exclui os arquivos setados pelo usuário com uma string
    através do parâmetro filtering.
    """
    for file in glob.glob(filtering):
        print(file)
        os.remove(file)

