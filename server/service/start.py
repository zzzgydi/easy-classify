# -*- coding: utf-8 -*-

import os
from core.context import Context, DB_PATH
from core.utils import TEMP_DIR, MODEL_DIR

sql_def_dataset = '''
CREATE TABLE dataset (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    label text NOT NULL,
    data text
);
'''

sql_def_model = '''
CREATE TABLE model (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    updated text NOT NULL
);
'''


def init_database():
    if os.path.exists(DB_PATH):
        return
    with Context() as ctx:
        ctx.exec(sql_def_dataset)
        ctx.exec(sql_def_model)


def init_model_path():
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    if not os.path.exists(MODEL_DIR):
        os.mkdir(MODEL_DIR)
