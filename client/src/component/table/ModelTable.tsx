import React from "react";
import { useAtom } from "jotai";
import { Table } from "antd";
import { ColumnsType } from "antd/lib/table";
import { modelAtom } from "@/state";

interface ModelTableProps {}

const ModelTable: React.FC<ModelTableProps> = (props) => {
  const [model] = useAtom(modelAtom);

  const columns: ColumnsType<any> = [
    {
      title: "名称",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "状态",
      dataIndex: "status",
      key: "status",
    },
    {
      title: "描述",
      dataIndex: "desc",
      key: "desc",
    },
    {
      title: "最后更新",
      dataIndex: "updated_time",
      key: "updated_time",
      width: "170px",
    },
  ];

  const pagination = {
    position: ["bottomCenter"],
  };

  return (
    <Table
      bordered
      rowKey="id"
      columns={columns}
      dataSource={model}
      pagination={pagination as any}
    />
  );
};

export default ModelTable;
