# -*- coding: utf-8 -*-
'''
dataset表的CURD
'''

from core.context import Context

sql_get_data = "select id, label, data from dataset where name=? order by id limit ? offset ?;"
sql_get_count = "select count(*) from dataset where name=?;"
sql_add_data = "insert into dataset (name, label, data) values (?,?,?);"
sql_del_data = 'delete from dataset where id=?;'
sql_get_name = 'select DISTINCT name from dataset;'
sql_get_label = 'select label, count(*) from dataset where name=? group by label;'


# 获取对应name的数据集的数据
def get_data(name: str, page: int, page_size: int) -> dict:
    offset = (page - 1) * page_size
    with Context() as ctx:
        if not ctx.exec(sql_get_data, (name, page_size, offset)):
            return None
        result = ctx.get_cursor().fetchall()
        if not ctx.exec(sql_get_count, (name, )):
            return None
        count = ctx.get_cursor().fetchone()[0]
        return {'result': result, 'count': count}


# 插入数据
def add_data(name: str, label: str, data: str) -> bool:
    with Context() as ctx:
        return ctx.exec(sql_add_data, (name, label, data))


# 批量插入数据
def add_many_data(name: str, label: str, data_list: list) -> bool:
    with Context() as ctx:
        for data in data_list:
            if not ctx.exec(sql_add_data, (name, label, data)):
                return False
        return True


# 删除数据
def del_data(data_id: str) -> bool:
    with Context() as ctx:
        return ctx.exec(sql_del_data, (data_id, ))


# 获取所有数据集的名称
def get_name() -> list:
    with Context() as ctx:
        if not ctx.exec(sql_get_name):
            return None
        result = ctx.get_cursor().fetchall()
        return [l[0] for l in result]


# 获取某数据集所有标签
def get_label(name: str) -> str:
    with Context() as ctx:
        if not ctx.exec(sql_get_label, (name, )):
            return None
        result = ctx.get_cursor().fetchall()
        return result
