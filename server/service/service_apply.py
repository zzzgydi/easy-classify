# -*- coding: utf-8 -*-

'''
模型应用
'''

import os
import fasttext

from core.words import CutByJieba
from core.lrucache import LRUCache
from core.utils import get_model_path
from service.curd_model import get_finish_model


MAX_NUM = 5
model_cache = LRUCache(MAX_NUM)  # LRU缓存模型数据
global_cutter = CutByJieba()     # 分词器


def run_apply(id: int, data_list: list, k: int) -> dict:
    ''' 预测一部分数据 '''
    model_data = model_cache.get(id)

    if model_data is None:
        # 获取模型数据
        result = get_finish_model(id)
        if result is None:
            return {'code': 500, 'msg': '找不到该模型数据'}

        mode_id = result.get('id')
        hash_name = result.get('hash')
        model_path = get_model_path(hash_name + '.ftz')
        if not os.path.exists(model_path):
            return {'code': 501, 'msg': '找不到该模型文件'}

        model_instance = fasttext.load_model(model_path)
        if not model_instance:
            return {'code': 502, 'msg': '模型文件启动失败'}

        # 在cache中添加该数据
        model_data = {'model_instance': model_instance, **result}
        model_cache.set(mode_id, model_data)

    model_instance = model_data['model_instance']
    # 预测数据
    data_list = [global_cutter.cut_words(line) for line in data_list]
    labels, scores = model_instance.predict(data_list, k=k)
    scores = [score.tolist() for score in scores]
    results = []
    for label, score in zip(labels, scores):
        results.append({'labels': label, 'scores': score})
    return {'code': 200, 'result': results}
