# -*- coding: utf-8 -*-


from flask import request, jsonify
from service import curd_dataset


# 获取所有数据集
def api_get_dataset():
    page = request.args.get('page', 1)
    page_size = request.args.get('pagesize', 100)
    page = int(page)
    page_size = int(page_size)
    res_dict = curd_dataset.get_dataset(page, page_size)
    if res_dict is None:
        return jsonify({'code': 500, 'msg': '数据读取错误'})
    return jsonify({'code': 200, **res_dict})


# 添加数据集 post
def api_add_dataset():
    req_json = request.get_json()
    name = req_json.get('name')
    desc = req_json.get('desc')
    if not name:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = curd_dataset.add_dataset(name, desc)
    if res:
        return jsonify({'code': 200})
    return jsonify({'code': 501, 'msg': '数据读写错误'})


# 删除数据集
def api_del_dataset():
    id = request.args.get('id')
    if not id:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = curd_dataset.del_dataset(id)
    if res:
        return jsonify({'code': 200})
    return jsonify({'code': 501, 'msg': '数据读写错误'})


# 更新数据集 post
def api_update_dataset():
    req_json = request.get_json()
    id = req_json.get('id')
    name = req_json.get('name')
    desc = req_json.get('desc')
    if not id or not name:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = curd_dataset.update_dataset(id, name, desc)
    if res:
        return jsonify({'code': 200})
    return jsonify({'code': 501, 'msg': '数据读写错误'})
