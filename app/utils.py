# -*- Coding: utf-8 -*-
from os import path

def file_exits(url_path):
    if path.isfile(url_path):
        return True
    return False