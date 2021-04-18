# -*- coding: utf-8 -*-

'''
模型训练服务
'''

import time
import random
import fasttext

from core.words import CutByJieba
from core.utils import get_temp_path, get_model_path

from service import curd_model


def run_train_task() -> bool:
    ''' 执行一次训练任务 '''
    try:
        task = curd_model.get_train_task()  # 拉取训练任务
        if not task:
            return False

        id = int(task.get('id'))
        hash_name = task.get('hash')

        # 确认训练任务 and 获取任务对应的数据
        task_data = curd_model.get_train_data(id)
        if not task_data:
            return False
        train_path = get_temp_path(hash_name + '.train')
        model_path = get_model_path(hash_name + '.ftz')

        cutter = CutByJieba(False)   # 使用分词器
        random.shuffle(task_data)    # 乱序数组

        def process_line(label, data):
            return '__label__{} {}'.format(label, cutter.cut_words(data))

        with open(train_path, 'w', encoding='utf8') as fwrite:
            results = [process_line(label, data) for label, data in task_data]
            fwrite.write('\n'.join(results))

        model = fasttext.train_supervised(train_path)
        model.save_model(model_path)

        curd_model.finish_train_task(id, {})
        return True
    except:
        return False


def main_train():
    ''' 不停地执行训练任务 '''
    while True:
        run_train_task()
        time.sleep(10)
