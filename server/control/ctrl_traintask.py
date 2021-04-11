# -*- coding: utf-8 -*-

from flask import request, jsonify
from service import curd_traintask


# 新建一个任务 post
def api_add_task():
    req_json = request.get_json()
    name = req_json.get('name')
    dataset = req_json.get('dataset')
    desc = req_json.get('desc')
    dataset = int(dataset)
    if not name or not dataset:
        return jsonify({'code': 400, 'msg': '参数错误'})

    res = curd_traintask.add_task(name, dataset, desc)
    if not res:
        return jsonify({'code': 500, 'msg': 'dataset不存在'})
    return jsonify({'code': 200})
