# -*- coding: utf-8 -*-
'''
CURD
'''

from core.context import Context
from core.utils import get_now_timestamp


'''
status: 
 - 0: 未开始
 - 1: 正在训练
 - 2: 已完成
'''


# 新建一个任务
def add_task(name: str, dataset: int, desc: str) -> bool:
    sql_get_dataset = 'select id from dataset where id=?;'
    sql_add_task = '''
        insert into traintask (name, dataset, status, desc, created_time, updated_time)
        values (?,?,?,?,?,?);
    '''
    now = get_now_timestamp()
    with Context() as ctx:
        if not ctx.exec(sql_get_dataset, (dataset, )):
            return False
        if not ctx.get_cursor().fetchone():
            return False
        return ctx.exec(sql_add_task, (name, dataset, 0, desc, now, now))


# 获取一个没开始的任务
def get_one_task() -> dict:
    sql_get_task = 'select * from traintask where status=0 order by id;'
    with Context() as ctx:
        if not ctx.exec(sql_get_task):
            return None
        task = ctx.get_cursor().fetchone()
        if not task:
            return None
        id, name, dataset, status, status_msg, desc, created_time, \
            updated_time = task[0]
        result = {
            'id': id, 'name': name, 'dataset': dataset,
            'status': status, 'status_msg': status_msg,
            'desc': desc, 'created_time': created_time,
            'updated_time': updated_time
        }
        return result


# 开始训练 修改状态
def get_task_data(id: int) -> list:
    sql_get_dataset = 'select dataset from traintask where id=? and status=0;'
    sql_update_status = 'update traintask set status=1, updated_time=? where id=? and status=0;'
    sql_get_labeldata = 'select label, data from labeldata where dataset=?;'
    now = get_now_timestamp()
    with Context() as ctx:
        if not ctx.exec(sql_get_dataset, (id, )):
            return None
        dataset = ctx.get_cursor().fetchone()
        if not dataset:
            return None
        if not ctx.exec(sql_update_status, (now, id)):
            return None
        if not ctx.exec(sql_get_labeldata, (dataset[0], )):
            return None
        task_data = ctx.get_cursor().fetchall()
        return task_data


# 完成训练
def finish_task(id: int) -> bool:
    sql_update_status = 'update traintask set status=2, updated_time=? where id=? and status=1;'
    now = get_now_timestamp()
    with Context() as ctx:
        return ctx.exec(sql_update_status, (now, id))
