import React, { useEffect, useState } from "react";
import { Row, Col, Select } from "antd";
import { apiGetDataset } from "../service/dataset";
import AppendModal from "../component/AppendModal";
import TrainModal from "../component/TrainModal";
import LabelTable from "../component/LabelTable";
import DataTable from "../component/DataTable";

const ManagePage: React.FC = () => {
  const [dataset, setDataset] = useState<string[]>([]); // 所有任务名
  const [name, setName] = useState<string>(""); // 当前任务名
  const [force, setForce] = useState<any>({});

  // 更新所有任务名
  const updateKeys = () => {
    apiGetDataset().then((res) => {
      setDataset(res.result);
      setName((n) => (n ? n : res.result[0] ?? ""));
    });
  };

  // 有新的数据更新
  const onAppendChange = () => {
    setForce({});
    updateKeys();
  };

  useEffect(() => {
    updateKeys();
  }, []);

  return (
    <div className="manage-page">
      <Row className="operate-box" align="middle">
        <Col flex="1 1 150px">
          <span>当前数据集：</span>
          <Select
            value={name}
            onChange={(val) => setName(val)}
            style={{ width: "calc(100% - 85px)", maxWidth: 200 }}
            options={dataset.map((v) => ({ label: v, value: v }))}
          />
        </Col>

        <Col flex="auto" />

        <Col style={{ marginRight: 10 }}>
          <TrainModal dataset={dataset} />
        </Col>

        <Col>
          <AppendModal onChange={onAppendChange} />
        </Col>
      </Row>

      <div className="label-box">
        <h2>标签</h2>
        <LabelTable name={name} force={force} />
      </div>

      <div className="table-box">
        <h2>数据</h2>
        <DataTable name={name} force={force} />
      </div>
    </div>
  );
};

export default ManagePage;
