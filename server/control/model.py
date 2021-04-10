# -*- coding: utf-8 -*-

from flask import request, jsonify
from service.model_train import TrainService
from service.model_apply import ApplyService

train_service: TrainService = None
apply_service: ApplyService = None


# 启动训练
def api_train_model():
    req_json = request.get_json()
    name = req_json.get('name')        # 该模型的名称
    dataset = req_json.get('dataset')  # 选择的数据集

    if not name or not dataset:
        return jsonify({'code': 400, 'msg': '参数错误'})

    global train_service
    if not train_service:
        train_service = TrainService()

    res = train_service.run_train(name, dataset)
    return jsonify({'code': 200 if res else 201})


# 进行模型预测 post 方法
def api_apply_model():
    req_json = request.get_json()
    name = req_json.get('name')
    data = req_json.get('data', [])
    k_value = req_json.get('k', 3)

    if not name:
        return jsonify({'code': 400, 'msg': '参数错误'})

    global apply_service
    if not apply_service:
        apply_service = ApplyService()

    try:
        res = apply_service.run_apply(name, data, k_value)
        return jsonify(res)
    except:
        return jsonify({'code': 500, 'msg': '未知错误'})
