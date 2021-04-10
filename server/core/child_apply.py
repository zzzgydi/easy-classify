# -*- coding: utf-8 -*-

'''
模型应用
'''

import os
import fasttext

from core.utils import get_model_path
from core.words import CutByJieba


def main_apply(conn):
    ''' 运行模型进程的函数 '''
    current_name = None
    current_model = None

    while True:
        # 获取信号
        recv_json: dict = conn.recv()
        signal = int(recv_json.get('signal', -1))
        payload: dict = recv_json.get('payload', {})

        # 小于0的信号关闭进程
        if signal < 0:
            return 0

        # 使用模型
        elif signal == 1:
            name = payload.get('name')
            data_list = payload.get('data', [])
            k_value = payload.get('k', 3)

            if not name:
                conn.send({'code': 600, 'msg': '缺少模型名称'})
                continue
            # 不是同一个模型则重新加载
            if name != current_name:
                model_path = get_model_path(name + '.ftz')

                if not os.path.exists(model_path):
                    conn.send({'code': 601, 'msg': '找不到该模型'})
                    continue

                current_name = name
                current_model = fasttext.load_model(model_path)

            if not current_model:
                conn.send({'code': 603, 'msg': '模型没有启动'})
                continue

            # 预测数据
            cutter = CutByJieba()  # 分词
            data_list = [cutter.cut_words(line) for line in data_list]
            labels, scores = current_model.predict(data_list, k=k_value)
            scores = [score.tolist() for score in scores]
            results = []
            for label, score in zip(labels, scores):
                results.append({'labels': label, 'scores': score})
            conn.send({'code': 200, 'result': results})
