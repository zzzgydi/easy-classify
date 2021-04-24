# -*- coding: utf-8 -*-
'''
CURD
'''

import json
from core.context import Context
from core.utils import get_random_str, get_now_timestamp


'''
status: 
 - 0: 未开始
 - 1: 正在训练
 - 2: 已完成
 - 3: 训练异常
'''


# 获取所有模型
def get_all_models(page: int, page_size: int) -> dict:
    sql_get_models = 'select * from model order by id limit ? offset ?;'
    sql_count_models = "select count(*) from model;"
    offset = (page - 1) * page_size
    with Context() as ctx:
        if not ctx.exec(sql_count_models):
            return None
        count = ctx.get_cursor().fetchone()[0]
        if not ctx.exec(sql_get_models, (page_size, offset)):
            return None
        item_list = ctx.get_cursor().fetchall()
        result = []
        for item in item_list:
            id, name, hash, dataset, status, info, desc, \
                created_time, updated_time = item
            result.append({
                'id': id,
                'name': name,
                'hash': hash,
                'dataset': dataset,
                'status': status,
                'info': info,
                'desc': desc,
                'created_time': created_time,
                'updated_time': updated_time
            })
        return {'count': count, 'result': result}


# 获取所有可用的模型
def get_valid_models() -> list:
    sql_get_valid_models = 'select * from model where status=2 order by id;'
    with Context() as ctx:
        if not ctx.exec(sql_get_valid_models):
            return None
        item_list = ctx.get_cursor().fetchall()
        result = []
        for item in item_list:
            id, name, hash, dataset, status, info, desc, \
                created_time, updated_time = item
            result.append({
                'id': id,
                'name': name,
                'hash': hash,
                'dataset': dataset,
                'status': status,
                'info': info,
                'desc': desc,
                'created_time': created_time,
                'updated_time': updated_time
            })
        return result


# 新建一个模型训练
def add_train_task(name: str, dataset: int, desc: str) -> bool:
    sql_get_dataset = 'select id from dataset where id=?;'
    sql_add_task = '''
        insert into model (name, hash, dataset, status, desc, created_time, updated_time)
        values (?,?,?,?,?,?,?);
    '''
    now = get_now_timestamp()
    hash_name = get_random_str(12)
    with Context() as ctx:
        if not ctx.exec(sql_get_dataset, (dataset, )):
            return False
        if not ctx.get_cursor().fetchone():
            return False
        return ctx.exec(sql_add_task, (name, hash_name, dataset, 0, desc, now, now))


# 获取一个模型训练任务
def get_train_task() -> dict:
    sql_get_task = 'select * from model where status=0 order by id;'
    with Context() as ctx:
        if not ctx.exec(sql_get_task):
            return None
        task = ctx.get_cursor().fetchone()
        if not task:
            return None
        id, name, hash, dataset, status, info, desc, \
            created_time, updated_time = task
        return {
            'id': id,
            'name': name,
            'hash': hash,
            'dataset': dataset,
            'status': status,
            'info': info,
            'desc': desc,
            'created_time': created_time,
            'updated_time': updated_time
        }


# 锁定一个模型训练任务 并 获取数据
def get_train_data(id: int) -> list:
    ''' 根据 '''
    sql_get_dataset = 'select dataset from model where id=? and status=0;'
    sql_update_status = 'update model set status=1, updated_time=? where id=? and status=0;'
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
def finish_train_task(id: int, info: dict) -> bool:
    sql_update_status = 'update model set status=2, info=?, updated_time=? where id=? and status=1;'
    now = get_now_timestamp()
    info = json.dumps(info)
    with Context() as ctx:
        return ctx.exec(sql_update_status, (info, now, id))


# 标记训练异常
def set_error_train(id: int):
    sql_error_status = 'update model set status=3, updated_time=? where id=?;'
    now = get_now_timestamp()
    with Context() as ctx:
        return ctx.exec(sql_error_status, (now, id))


# 根据id获取已经完成的模型数据
def get_finish_model(id: int) -> dict:
    sql_get_model = 'select * from model where id=? and status=2;'
    with Context() as ctx:
        if not ctx.exec(sql_get_model, (id, )):
            return None
        task = ctx.get_cursor().fetchone()
        if not task:
            return None
        id, name, hash, dataset, status, info, desc, \
            created_time, updated_time = task[0]
        return {
            'id': id,
            'name': name,
            'hash': hash,
            'dataset': dataset,
            'status': status,
            'info': info,
            'desc': desc,
            'created_time': created_time,
            'updated_time': updated_time
        }
