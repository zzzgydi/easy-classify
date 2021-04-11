import React, { useState } from "react";
import { Modal, Button, Form, Input, message } from "antd";
import datasetApi from "../service/dataset";

interface DatasetModalProps {
  onChange?: () => void;
}

const DatasetModal: React.FC<DatasetModalProps> = (props) => {
  const { onChange } = props;

  const [visible, setVisible] = useState(false);
  const [form] = Form.useForm();

  const handleOk = async () => {
    const formResult = await form.validateFields();
    const { name, desc } = formResult;

    datasetApi
      .add(name, desc)
      .then(() => {
        onChange?.();
        setVisible(false);
        form.resetFields();
        message.success("添加成功");
      })
      .catch(() => message.error("添加失败"));
  };

  return (
    <>
      <Button type="primary" onClick={() => setVisible(true)}>
        添加数据集
      </Button>

      <Modal
        title="添加数据集"
        visible={visible}
        width={800}
        okText="确认"
        cancelText="取消"
        onOk={handleOk}
        onCancel={() => setVisible(false)}
      >
        <Form form={form} labelCol={{ span: 3 }}>
          <Form.Item
            label="数据集名称"
            name="name"
            rules={[
              { required: true, message: "数据集名称必填" },
              { pattern: /^\S+$/, message: "数据集名称不支持空白字符" },
            ]}
          >
            <Input placeholder="数据集 支持任意非空白字符" />
          </Form.Item>

          <Form.Item label="数据集描述" name="desc">
            <Input.TextArea rows={5} placeholder="请输入数据集的描述信息" />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default DatasetModal;
