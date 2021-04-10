# -*- coding: utf-8 -*-

'''
负责模型训练
'''

import random
import fasttext

from core.utils import get_temp_path, get_model_path
from core.words import CutByJieba, CutByBlank
from core.context import Context


def dump_train_data(path: str, dataset: str):
    ''' 将对应key的数据保存到路径 '''
    sql_select = 'select label, data from dataset where name = ?;'
    results: list = []
    with Context() as ctx:
        if not ctx.exec(sql_select, (dataset, )):
            raise Exception('context error')
        results = ctx.get_cursor().fetchall()

    cutter = CutByJieba(False)   # 使用分词器

    def process_line(label: str, data: str):
        return '__label__{} {}'.format(label, cutter.cut_words(data))

    with open(path, 'w', encoding='utf8') as fwrite:
        results = [process_line(label, data) for label, data in results]
        random.shuffle(results)
        fwrite.write('\n'.join(results))
    pass


def main_train(conn):
    ''' 执行训练进程的函数 '''
    recv: dict = conn.recv()

    name = recv.get('name')
    dataset = recv.get('dataset')

    # p_lr = int(recv.get('lr', 0.1))
    # p_dim = int(recv.get('dim', 100))
    # p_ws = int(recv.get('ws', 5))
    # p_epoch = int(recv.get('epoch', 5))
    # p_wordNgrams = int(recv.get('wordNgrams', 2))

    if not name or not dataset:
        return 1
    try:
        temp_path = get_temp_path(name + '.train')
        model_path = get_model_path(name + '.ftz')
        dump_train_data(temp_path, dataset)
        # model = fasttext.train_supervised(temp_path, lr=p_lr, dim=p_dim, ws=p_ws,
        #                                   epoch=p_epoch, wordNgrams=p_wordNgrams)
        model = fasttext.train_supervised(temp_path)
        model.save_model(model_path)
        return 0
    except:
        return 2
