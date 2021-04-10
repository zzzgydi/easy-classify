# -*- coding: utf-8 -*-
'''

工具模块

'''
import os
import re


TEMP_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../../data/temp'))
MODEL_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../../data/model'))


def get_temp_path(name: str) -> str:
    ''' 获取训练文件暂存路径 '''
    return os.path.join(TEMP_DIR, name)


def get_model_path(name: str) -> str:
    ''' 获取模型存储路径 '''
    return os.path.join(MODEL_DIR, name)


def list_model_dir() -> list:
    if not os.path.exists(MODEL_DIR):
        return []
    file_list = os.listdir(MODEL_DIR)
    re_ftz = re.compile(r'\..+$')
    file_list = [re_ftz.sub('', file)
                 for file in file_list if re_ftz.search(file)]
    return file_list
