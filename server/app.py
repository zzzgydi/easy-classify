# -*- coding: utf-8 -*-

from flask import Flask

from service.start import init_database, init_model_path
import control.dataset as ctl_dataset
import control.model as ctl_model

app = Flask(__name__)


# 数据集相关
app.add_url_rule('/api/data', view_func=ctl_dataset.api_get_data,
                 methods=['GET'])
app.add_url_rule('/api/data', view_func=ctl_dataset.api_add_many_data,
                 methods=['POST'])
app.add_url_rule('/api/data', view_func=ctl_dataset.api_del_data,
                 methods=['DELETE'])
app.add_url_rule('/api/dataset', view_func=ctl_dataset.api_get_name,
                 methods=['GET'])
app.add_url_rule('/api/label', view_func=ctl_dataset.api_get_label,
                 methods=['GET'])
app.add_url_rule('/api/model', view_func=ctl_dataset.api_get_model,
                 methods=['GET'])


# 模型相关
app.add_url_rule('/api/train', view_func=ctl_model.api_train_model,
                 methods=['POST'])
app.add_url_rule('/api/apply', view_func=ctl_model.api_apply_model,
                 methods=['POST'])


if __name__ == '__main__':
    init_database()
    init_model_path()
    app.run()
