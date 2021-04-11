# -*- coding: utf-8 -*-

from flask import request, jsonify
from service import curd_labeldata


# 获取某个数据集的所有数据
def api_get_labeldata():
    dataset = request.args.get('dataset')
    page = request.args.get('page', 1)
    page_size = request.args.get('pagesize', 100)
    if not dataset:
        return jsonify({'code': 400, 'msg': '参数错误'})
    dataset = int(dataset)
    page = int(page)
    page_size = int(page_size)
    res_dict = curd_labeldata.get_labeldata(dataset, page, page_size)
    if res_dict is None:
        return jsonify({'code': 500, 'msg': '数据读取错误'})
    return jsonify({'code': 200, **res_dict})


# 获取数据集的所有标签数据统计
def api_get_labelinfo():
    dataset = request.args.get('dataset')
    if not dataset:
        return jsonify({'code': 400, 'msg': '参数错误'})
    result = curd_labeldata.get_label_info(dataset)
    return jsonify({'code': 200, 'result': result})


# 批量添加数据
def api_add_many_data():
    res_json = request.get_json()
    dataset = res_json.get('dataset')
    label = res_json.get('label')
    data_list = res_json.get('datalist')

    if not dataset or not label or not data_list:
        return jsonify({'code': 400, 'msg': '参数错误'})
    try:
        dataset = int(dataset)
        res = curd_labeldata.add_labeldata(dataset, label, data_list)
        return jsonify({'code': 200 if res else 500})
    except:
        return jsonify({'code': 500, 'msg': '数据异常'})


# 删除数据
def api_del_data():
    id = request.args.get('id')
    if not id:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = curd_labeldata.del_dataset(int(id))
    return jsonify({'code': 200 if res else 500})
