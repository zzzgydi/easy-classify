# -*- coding: utf-8 -*-

'''
模型调用服务
'''

from multiprocessing import Pipe, Process
from core.child_apply import main_apply


class ApplyService:
    process: Process = None
    parent_conn = None

    def __init__(self):
        pass

    def is_alive(self):
        return self.process and self.process.is_alive()

    def start(self):
        if self.is_alive():
            return
        parent_conn, child_conn = Pipe()
        self.parent_conn = parent_conn
        self.process = Process(target=main_apply, args=(child_conn, ))
        self.process.start()

    def run_apply(self, name: str, data: list, k: int) -> dict:
        ''' 执行预测 '''
        self.start()
        payload = {'name': name, 'data': data, 'k': k}
        params = {'signal': 1, 'payload': payload}
        self.parent_conn.send(params)
        try:
            recv = self.parent_conn.recv()
            return recv
        except Exception as e:
            print(e)
            return {'code': 500, 'msg': '未知错误'}
