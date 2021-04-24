import React from "react";
import { useAtom } from "jotai";
import { Button, Space } from "antd";
import { updateDatasetAtom } from "@/state";
import DatasetModal from "@/component/modal/DatasetModal";
import DatasetTable from "@/component/table/DatasetTable";

const DatasetPage: React.FC = () => {
  const [, updateDataset] = useAtom(updateDatasetAtom);

  return (
    <div className="dataset-page">
      <div className="header-box">
        <div className="title">数据集管理</div>

        <Space size="middle">
          <Button onClick={() => updateDataset(true)}>刷新</Button>
          <DatasetModal />
        </Space>
      </div>

      <div className="main-box">
        <DatasetTable />
      </div>
    </div>
  );
};

export default DatasetPage;
