# -*- coding: utf-8 -*-
'''
CURD
'''

from core.context import Context
from core.utils import get_now_timestamp


# 获取所有数据集的信息
def get_dataset(page: int, page_size: int) -> list:
    sql_get_dataset = 'select * from dataset order by id limit ? offset ?;'
    sql_count_dataset = 'select count(*) from dataset;'
    offset = (page - 1) * page_size
    with Context() as ctx:
        if not ctx.exec(sql_get_dataset, (page_size, offset)):
            return None
        result = ctx.get_cursor().fetchall()
        if not ctx.exec(sql_count_dataset):
            return None
        count = ctx.get_cursor().fetchone()[0]
        return {'result': result, 'count': count}


# 添加数据集
def add_dataset(name: str, desc: str) -> bool:
    sql_add_dataset = 'insert into dataset (name, desc, updated_time) values (?,?,?);'
    now = get_now_timestamp()
    with Context() as ctx:
        return ctx.exec(sql_add_dataset, (name, desc, now))


# 删除数据集
def del_dataset(id: int) -> bool:
    sql_del_dataset = 'delete from dataset where id=?;'
    sql_del_all_labeldata = 'delete from labeldata where dataset=?;'
    with Context() as ctx:
        return ctx.exec(sql_del_dataset, (id, )) and \
            ctx.exec(sql_del_all_labeldata, (id, ))


# 更新数据集
def update_dataset(id: int, name: str, desc: str) -> bool:
    sql_update_dataset = 'update dataset set name=?, desc=?, updated_time=? where id=?;'
    now = get_now_timestamp()
    with Context() as ctx:
        return ctx.exec(sql_update_dataset, (name, desc, now, id))
