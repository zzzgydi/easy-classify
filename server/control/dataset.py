# -*- coding: utf-8 -*-

from flask import request, jsonify
from core.utils import list_model_dir
from service import dataset as service


# 获取对应name的数据集的数据
def api_get_data():
    name = request.args.get('name')
    page = request.args.get('page', 1)
    page_size = request.args.get('pagesize', 100)

    if not name:
        return jsonify({'code': 400, 'msg': '参数错误'})
    page = int(page)
    page_size = int(page_size)
    res_dict = service.get_data(name, page, page_size)
    if res_dict is None:
        return jsonify({'code': 500, 'msg': '数据读取错误'})
    return jsonify({'code': 200, **res_dict})


# 批量插入数据
def api_add_many_data():
    res_json = request.get_json()
    name = res_json.get('name')
    label = res_json.get('label')
    data_list = res_json.get('datalist')

    if not label or not data_list or not name:
        return jsonify({'code': 400, 'msg': '参数错误'})
    try:
        res = service.add_many_data(name, label, data_list)
        return jsonify({'code': 200 if res else 500})
    except:
        return jsonify({'code': 500, 'msg': '数据异常'})


# 删除数据
def api_del_data():
    data_id = request.args.get('id')
    if not data_id:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = service.del_data(int(data_id))
    return jsonify({'code': 200 if res else 500})


# 获取所有数据集的名称
def api_get_name():
    result = service.get_name()
    if result is None:
        return jsonify({'code': 500})
    return jsonify({'code': 200, 'result': result})


# 获取数据集的所有标签
def api_get_label():
    name = request.args.get('name')
    if not name:
        return jsonify({'code': 400, 'msg': '参数错误'})
    result = service.get_label(name)
    return jsonify({'code': 200, 'result': result})


# 获取所有可用的模型
def api_get_model():
    file_list = list_model_dir()
    return jsonify({'code': 200, 'result': file_list})
