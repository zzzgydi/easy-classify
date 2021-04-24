import React, { useEffect, useState } from "react";
import { Table, message } from "antd";
import { ColumnsType } from "antd/lib/table";
import labeldataApi from "@/service/labeldata";

const DEFAULT_PAGE_SIZE = 10;

interface DataTableProps {
  datasetId: number;
  force: any;
  onChange: () => void;
}

const DataTable: React.FC<DataTableProps> = (props) => {
  const { datasetId, force, onChange } = props;

  const [total, setTotal] = useState<number>(0);
  const [page, setPage] = useState<number>(1);
  const [pageSize, setPageSize] = useState<number>(DEFAULT_PAGE_SIZE);
  const [dataSource, setDataSource] = useState<any[]>([]);

  const updateData = (current: number, size: number) => {
    if (!datasetId) return;

    labeldataApi.list(datasetId, current, size).then((res) => {
      const { result, count } = res;
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
    labeldataApi
      .remove(id)
      .then(() => {
        message.success("删除成功");
        onChange();
      })
      .catch(() => message.error("删除失败"));
  };

  useEffect(() => forceUpdate(), [force, datasetId]);

  const columns: ColumnsType<any> = [
    {
      title: "标签",
      dataIndex: "label",
      key: "label",
      width: "120px",
    },
    {
      title: "数据",
      dataIndex: "data",
      key: "data",
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
      columns={columns}
      dataSource={dataSource}
      pagination={pagination as any}
    />
  );
};

export default DataTable;
