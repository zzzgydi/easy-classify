import React, { useEffect, useState } from "react";
import { Row, Col, Select } from "antd";
import AppendModal from "../component/AppendModal";
import TrainModal from "../component/TrainModal";
import LabelTable from "../component/LabelTable";
import DataTable from "../component/DataTable";
import datasetApi, { DatasetModel } from "@/service/dataset";

const ManagePage: React.FC = () => {
  const [dataset, setDataset] = useState<DatasetModel[]>([]); // 所有数据集
  const [datasetId, setDatasetId] = useState<number>(); // 当前数据集
  const [force, setForce] = useState<any>({});

  // 更新所有数据集
  const updateKeys = () => {
    datasetApi.list(1, 9999).then((res) => {
      setDataset(res.result);
      const { id } = res.result[0] || {};
      setDatasetId((v) => (v != null ? v : id));
    });
  };

  // 有新的数据更新
  const onAppendChange = () => {
    setForce({});
    updateKeys();
  };

  useEffect(() => updateKeys(), []);

  return (
    <div className="manage-page">
      <Row className="operate-box" align="middle">
        <Col flex="1 1 150px">
          <span>当前数据集：</span>
          <Select
            value={datasetId}
            onChange={(val) => setDatasetId(val)}
            style={{ width: "calc(100% - 85px)", maxWidth: 200 }}
            options={dataset.map((v) => ({ label: v.name, value: v.id }))}
          />
        </Col>

        <Col flex="auto" />

        <Col style={{ marginRight: 10 }}>
          <TrainModal dataset={dataset} />
        </Col>

        <Col>
          <AppendModal dataset={dataset} onChange={onAppendChange} />
        </Col>
      </Row>

      <div className="table-box">
        <h2>数据列表</h2>

        <div style={{ marginBottom: 20 }}>
          <LabelTable datasetId={datasetId!} force={force} />
        </div>

        <DataTable datasetId={datasetId!} force={force} />
      </div>
    </div>
  );
};

export default ManagePage;
