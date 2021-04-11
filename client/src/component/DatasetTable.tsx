import React, { useEffect, useState } from "react";
import { Modal, Table, message } from "antd";
import { ColumnsType } from "antd/lib/table";
import datasetApi from "../service/dataset";

const DEFAULT_PAGE_SIZE = 10;

interface DatasetTableProps {
  force: any;
}

const DatasetTable: React.FC<DatasetTableProps> = (props) => {
  const { force } = props;

  const [total, setTotal] = useState<number>(0);
  const [page, setPage] = useState<number>(1);
  const [pageSize, setPageSize] = useState<number>(DEFAULT_PAGE_SIZE);
  const [dataSource, setDataSource] = useState<any[]>([]);

  const updateData = (current: number, size: number) => {
    datasetApi.list(current, size).then(({ result, count }) => {
      setTotal(count);
      setDataSource(result);
    });
  };

  const forceUpdate = () => {
    setPage(1);
    setPageSize(DEFAULT_PAGE_SIZE);
    updateData(1, DEFAULT_PAGE_SIZE);
  };

  const onDeleteData = (id: number) => {
    Modal.confirm({
      content: "删除数据集同时删除对应的数据",
      okText: "确认删除",
      cancelText: "取消",
      centered: true,
      maskClosable: true,
      onOk: () => {
        datasetApi
          .remove(id)
          .then(() => {
            updateData(page, pageSize);
            message.success("删除成功");
          })
          .catch(() => message.error("删除失败"));
      },
    });
  };

  useEffect(() => forceUpdate(), [force]);

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
      dataIndex: "updated",
      key: "updated",
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
    total,
    current: page,
    pageSize,
    position: ["bottomCenter"],
    onChange: (current: number, size: number) => {
      setPage(current);
      setPageSize(size);
      updateData(current, size);
    },
  };

  return (
    <Table
      bordered
      rowKey="id"
      dataSource={dataSource}
      columns={columns}
      pagination={pagination as any}
    />
  );
};

export default DatasetTable;
