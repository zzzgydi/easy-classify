import React from "react";
import { useAtom } from "jotai";
import { Modal, Table, message } from "antd";
import { ColumnsType } from "antd/lib/table";
import { datasetAtom } from "@/state";
import datasetApi from "@/service/dataset";

interface DatasetTableProps {}

const DatasetTable: React.FC<DatasetTableProps> = (props) => {
  const [dataset, setDataset] = useAtom(datasetAtom);

  const onDeleteData = (id: number) => {
    Modal.confirm({
      content: "删除数据集同时删除对应的数据",
      okText: "确认删除",
      cancelText: "取消",
      centered: true,
      maskClosable: true,
      onOk: () => {
        const deleteDataset = async (id: number) => {
          await datasetApi.remove(id);
          setDataset((list: any[]) => {
            const index = list.findIndex((value) => value.id === id);
            if (index === -1) return list;
            list.splice(index, 1);
            return [...list];
          });
        };

        deleteDataset(id)
          .then(() => message.success("删除成功"))
          .catch(() => message.error("删除失败"));
      },
    });
  };

  const columns: ColumnsType<any> = [
    {
      title: "名称",
      dataIndex: "name",
      key: "name",
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
    {
      title: "操作",
      dataIndex: "id",
      width: "100px",
      align: "center",
      render: (id: number) => {
        return <a onClick={() => onDeleteData(id)}>删除</a>;
      },
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
      dataSource={dataset}
      pagination={pagination as any}
    />
  );
};

export default DatasetTable;
