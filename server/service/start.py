# -*- coding: utf-8 -*-

import os
from core.context import Context, DB_PATH
from core.utils import DATA_DIR, TEMP_DIR, MODEL_DIR

sql_def_dataset = '''
CREATE TABLE dataset (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    desc text,
    updated_time int NOT NULL
);
'''

# 记录每一个标注的数据
sql_def_labeldata = '''
CREATE TABLE labeldata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset int NOT NULL,
    label text NOT NULL,
    data text
);
'''

# 记录每一个模型的状态
sql_def_model = '''
CREATE TABLE model (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    hash text NOT NULL,
    dataset int NOT NULL,
    status int NOT NULL,
    info text,
    desc text,
    created_time int NOT NULL,
    updated_time int NOT NULL
);
'''


def init_server():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    if not os.path.exists(MODEL_DIR):
        os.mkdir(MODEL_DIR)
    if not os.path.exists(DB_PATH):
        with Context() as ctx:
            ctx.exec(sql_def_dataset)
            ctx.exec(sql_def_labeldata)
            ctx.exec(sql_def_model)
