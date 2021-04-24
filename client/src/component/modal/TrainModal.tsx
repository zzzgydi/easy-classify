import React, { useState } from "react";
import { Modal, Button, Form, Input, message, Select } from "antd";
import { useAtom } from "jotai";
import { datasetAtom, updateModelAtom } from "@/state";
import modelApi from "@/service/model";

interface TrainModalProps {}

const TrainModal: React.FC<TrainModalProps> = (props) => {
  const [form] = Form.useForm();
  const [dataset] = useAtom(datasetAtom);
  const [, updateModel] = useAtom(updateModelAtom);
  const [visible, setVisible] = useState(false);

  const handleOk = async () => {
    const formResult = await form.validateFields();

    modelApi
      .train(formResult.name, formResult.dataset, formResult.desc)
      .then(({ code }) => {
        if (code === 200) {
          updateModel(true);
          setVisible(false);
          form.resetFields();
        }
      });
  };

  return (
    <>
      <Button type="primary" onClick={() => setVisible(true)}>
        开始训练
      </Button>

      <Modal
        title="开始训练"
        visible={visible}
        okText="确认"
        cancelText="取消"
        onOk={handleOk}
        onCancel={() => setVisible(false)}
      >
        <Form form={form} name="train" labelCol={{ span: 4 }}>
          <Form.Item
            label="模型名"
            name="name"
            rules={[
              { required: true, message: "模型名必填" },
              { pattern: /^\S+$/, message: "模型名不支持空白字符" },
            ]}
          >
            <Input placeholder="模型名 支持任意非空白字符" />
          </Form.Item>

          <Form.Item
            label="数据集"
            name="dataset"
            rules={[{ required: true, message: "数据集必选" }]}
          >
            <Select
              placeholder="请选择训练的数据集"
              options={dataset.map((v) => ({ label: v.name, value: v.id }))}
            />
          </Form.Item>

          <Form.Item label="简要描述" name="desc">
            <Input placeholder="请输入该模型的简要描述信息" />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default TrainModal;
