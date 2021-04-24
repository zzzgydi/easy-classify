import React, { useState } from "react";
import { useAtom } from "jotai";
import { Modal, Button, Form, Input, message, Select } from "antd";
import { datasetAtom } from "@/state";
import labeldataApi from "@/service/labeldata";

interface DataModalProps {
  onChange: () => void;
}

// 新增数据
const DataModal: React.FC<DataModalProps> = (props) => {
  const { onChange } = props;

  const [dataset] = useAtom(datasetAtom);
  const [visible, setVisible] = useState(false);
  const [form] = Form.useForm();

  const handleOk = async () => {
    const formResult = await form.validateFields();
    const { datasetId, label, data } = formResult;
    const datalist = data.split("\n").filter((e: string) => e && e.trim());

    labeldataApi
      .add(datasetId, label, datalist)
      .then(() => {
        onChange();
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
        <Form form={form} name="data" labelCol={{ span: 3 }}>
          <Form.Item
            label="数据集"
            name="datasetId"
            rules={[{ required: true, message: "数据集名称必填" }]}
          >
            <Select
              style={{ width: "100%" }}
              placeholder="请选择对应的数据集"
              options={dataset.map((v) => ({ label: v.name, value: v.id }))}
            />
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
              style={{ whiteSpace: "nowrap" }}
            />
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default DataModal;
