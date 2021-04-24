# -*- coding: utf-8 -*-

'''
模型训练服务
'''

import time
import random
import fasttext

from multiprocessing import Process
from core.words import CutByJieba
from core.utils import get_temp_path, get_model_path
from service import curd_model


def run_train_task() -> bool:
    ''' 执行一次训练任务 '''

    task = curd_model.get_train_task()  # 拉取训练任务
    if not task:
        return False

    id = int(task.get('id'))
    hash_name = task.get('hash')

    print('[Train Info]: prepare to train task {} [{}]'.format(id, hash_name))

    try:
        # 确认训练任务 and 获取任务对应的数据
        task_data = curd_model.get_train_data(id)
        if not task_data:
            return False
        train_path = get_temp_path(hash_name + '.train')
        model_path = get_model_path(hash_name + '.ftz')

        cutter = CutByJieba()   # 使用分词器
        random.shuffle(task_data)    # 乱序数组

        def process_line(label, data):
            return '__label__{} {}'.format(label, cutter.cut_words(data))

        with open(train_path, 'w', encoding='utf8') as fwrite:
            results = [process_line(label, data) for label, data in task_data]
            fwrite.write('\n'.join(results))

        print('[Train Info]: Begin to train task {} [{}] *'.format(id, hash_name))

        model = fasttext.train_supervised(train_path)
        model.save_model(model_path)

        curd_model.finish_train_task(id, {})
        return True
    except Exception as e:
        print('[Train Error]:', e)
        curd_model.set_error_train(id)
        return False


def main_train():
    ''' 不停地执行训练任务 '''
    while True:
        print('[Train Info]: Heart beating...')
        run_train_task()
        time.sleep(5)


def run_train_process():
    ''' 新建进程 '''
    process = Process(target=main_train)
    process.start()  # 启动训练进程的函数
