# -*- coding: utf-8 -*-
'''
CURD
'''

from core.context import Context


# 获取某个数据集的所有数据
def get_labeldata(dataset: int, page: int, page_size: int) -> list:
    sql_get_labeldata = "select id, label, data from labeldata where dataset=? order by id limit ? offset ?;"
    sql_count_labeldata = "select count(*) from labeldata where dataset=?;"
    offset = (page - 1) * page_size
    with Context() as ctx:
        if not ctx.exec(sql_get_labeldata, (dataset, page_size, offset)):
            return None
        result = ctx.get_cursor().fetchall()
        if not ctx.exec(sql_count_labeldata, (dataset, )):
            return None
        count = ctx.get_cursor().fetchone()[0]
        return {'result': result, 'count': count}


# 获取数据集的所有标签数据统计
def get_label_info(dataset: int) -> list:
    sql_get_info = 'select label, count(*) from labeldata where dataset=? group by label;'
    with Context() as ctx:
        if not ctx.exec(sql_get_info, (dataset, )):
            return None
        result = ctx.get_cursor().fetchall()
        return result


# 批量添加数据
def add_labeldata(dataset: int, label: str, data_list: list) -> bool:
    sql_search_dataset = 'select id from dataset where id=?;'
    sql_add_labeldata = "insert into labeldata (dataset, label, data) values (?,?,?);"
    with Context() as ctx:
        if not ctx.exec(sql_search_dataset, (dataset, )):
            return False
        # 没有该id不加数据
        if not ctx.get_cursor().fetchone():
            return False
        for data in data_list:
            if not ctx.exec(sql_add_labeldata, (dataset, label, data)):
                return False
        return True


# 删除数据
def del_dataset(id: int) -> bool:
    sql_del_labeldata = 'delete from labeldata where id=?;'
    with Context() as ctx:
        return ctx.exec(sql_del_labeldata, (id, ))
