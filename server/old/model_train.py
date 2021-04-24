# -*- coding: utf-8 -*-

'''
模型训练服务
'''

from multiprocessing import Pipe, Process
from core.child_train import main_train


class TrainService:
    process: Process = None
    parent_conn = None

    def __init__(self):
        pass

    def is_alive(self):
        return self.process and self.process.is_alive()

    def start(self):
        if self.is_alive():  # 一次仅一个训练进程
            return
        parent_conn, child_conn = Pipe()
        self.parent_conn = parent_conn
        self.process = Process(target=main_train, args=(child_conn, ))
        self.process.start()  # 启动训练进程的函数

    def run_train(self, name: str, dataset: str, lr=0.1, dim=100, ws=5, epoch=5, wordNgrams=1) -> bool:
        ''' 执行训练 '''
        self.start()
        params = {
            'name': name,
            'dataset': dataset,
            'lr': lr,
            'dim': dim,
            'ws': ws,
            'epoch': epoch,
            'wordNgrams': wordNgrams,
        }
        self.parent_conn.send(params)
        return True
