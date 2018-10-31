# coding: utf-8

import os
import glob


def current_directory():
    return os.getcwd()


def browser(dir):
    return os.chdir(dir)


def to_cleaner(char):
    for file in glob.glob(char):
        print(file)
        os.remove(file)

