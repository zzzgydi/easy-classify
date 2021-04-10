import React, { useState } from "react";
import { Modal, Button, Form, Input, message } from "antd";
import { apiAddData } from "../service/dataset";

interface AppendModalProps {
  onChange?: () => void;
}

const AppendModal: React.FC<AppendModalProps> = (props) => {
  const { onChange } = props;

  const [visible, setVisible] = useState(false);
  const [form] = Form.useForm();

  const handleOk = async () => {
    const formResult = await form.validateFields();
    const { name, label, data } = formResult;
    const datalist = data.split("\n").filter((e: string) => e && e.trim());

    apiAddData(name, label, datalist)
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
        添加数据
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
            label="数据集"
            name="name"
            rules={[
              { required: true, message: "数据集名称必填" },
              { pattern: /^\S+$/, message: "数据集名称不支持空白字符" },
            ]}
          >
            <Input placeholder="数据集 支持任意非空白字符" />
          </Form.Item>

          <Form.Item
            label="标签名"
            name="label"
            rules={[
              { required: true, message: "标签名必填" },
              { pattern: /^\S+$/, message: "标签名不支持空白字符" },
            ]}
          >
            <Input placeholder="标签名 支持任意非空白字符" />
          </Form.Item>

          <Form.Item
            label="多行数据"
            name="data"
            rules={[{ required: true, message: "至少输入一行数据" }]}
          >
            <Input.TextArea
              rows={5}
              placeholder="换行输入多条数据"
              style={{ wordWrap: "normal" }}
            />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default AppendModal;
