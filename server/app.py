# -*- coding: utf-8 -*-

from flask import Flask

from service.start import init_server
from control import ctrl_dataset, ctrl_labeldata, ctrl_traintask

app = Flask(__name__)


# 数据集相关
app.add_url_rule('/api/dataset', view_func=ctrl_dataset.api_get_dataset,
                 methods=['GET'])
app.add_url_rule('/api/dataset', view_func=ctrl_dataset.api_add_dataset,
                 methods=['POST'])
app.add_url_rule('/api/dataset', view_func=ctrl_dataset.api_del_dataset,
                 methods=['DELETE'])
app.add_url_rule('/api/dataset/update', view_func=ctrl_dataset.api_update_dataset,
                 methods=['POST'])

# 数据相关
app.add_url_rule('/api/data', view_func=ctrl_labeldata.api_get_labeldata,
                 methods=['GET'])
app.add_url_rule('/api/data', view_func=ctrl_labeldata.api_add_many_data,
                 methods=['POST'])
app.add_url_rule('/api/data', view_func=ctrl_labeldata.api_del_data,
                 methods=['DELETE'])
app.add_url_rule('/api/data/label', view_func=ctrl_labeldata.api_get_labelinfo,
                 methods=['GET'])

# 训练相关
app.add_url_rule('/api/train', view_func=ctrl_traintask.api_add_task,
                 methods=['POST'])

# app.add_url_rule('/api/data', view_func=ctl_dataset.api_get_data,
#                  methods=['GET'])
# app.add_url_rule('/api/data', view_func=ctl_dataset.api_add_many_data,
#                  methods=['POST'])
# app.add_url_rule('/api/data', view_func=ctl_dataset.api_del_data,
#                  methods=['DELETE'])
# app.add_url_rule('/api/dataset', view_func=ctl_dataset.api_get_name,
#                  methods=['GET'])
# app.add_url_rule('/api/label', view_func=ctl_dataset.api_get_label,
#                  methods=['GET'])
# app.add_url_rule('/api/model', view_func=ctl_dataset.api_get_model,
#                  methods=['GET'])


# # 模型相关
# app.add_url_rule('/api/train', view_func=ctl_model.api_train_model,
#                  methods=['POST'])
# app.add_url_rule('/api/apply', view_func=ctl_model.api_apply_model,
#                  methods=['POST'])


if __name__ == '__main__':
    init_server()
    app.run(debug=True)
