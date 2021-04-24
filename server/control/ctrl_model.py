# -*- coding: utf-8 -*-

from flask import request, jsonify
from service import curd_model, service_apply


# 获取所有模型
def api_get_models():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pagesize', 100))
    result = curd_model.get_all_models(page, page_size)
    if not result:
        return jsonify({'code': 500, 'msg': '获取数据出错'})
    return jsonify({'code': 200, **result})


# 获取所有可用的模型
def api_get_valid_models():
    result = curd_model.get_valid_models()
    if not result:
        return jsonify({'code': 500, 'msg': '获取数据出错'})
    return jsonify({'code': 200, 'result': result})


# 新建一个任务 post
def api_add_train_task():
    req_json = request.get_json()
    name = req_json.get('name')
    dataset = req_json.get('dataset')
    desc = req_json.get('desc')
    if not name or not dataset:
        return jsonify({'code': 400, 'msg': '参数错误'})
    res = curd_model.add_train_task(name, int(dataset), desc)
    if not res:
        return jsonify({'code': 500, 'msg': 'dataset不存在'})
    return jsonify({'code': 200})


# 获取模型训练任务
def api_get_train_task():
    result = curd_model.get_train_task()
    if not result:
        return jsonify({'code': 500, 'msg': '暂无任务'})
    return jsonify({'code': 200, 'result': result})


# 锁定模型训练任务 并 获取数据
def api_get_train_data():
    dataset = int(request.args.get('dataset'))
    result = curd_model.get_train_data(dataset)
    if not result:
        return jsonify({'code': 500, 'msg': '获取数据出错'})
    return jsonify({'code': 200, 'result': result})


# 完成模型任务
def api_finish_train_task():
    req_json = request.get_json()
    id = req_json.get('id')
    info = req_json.get('info')
    if not id:
        return jsonify({'code': 400, 'msg': '参数错误'})
    result = curd_model.finish_train_task(int(id), info)
    return jsonify({'code': 200 if result else 500})


# 应用模型任务
def api_apply_model():
    req_json = request.get_json()
    id = req_json.get('id')
    data_list = req_json.get('data', [])
    k = req_json.get('k', 3)

    if not id:
        return jsonify({'code': 400, 'msg': '参数错误'})
    result = service_apply.run_apply(int(id), data_list, k)
    return jsonify(result)
