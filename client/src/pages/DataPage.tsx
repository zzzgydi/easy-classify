import React, { useEffect, useState } from "react";
import { useAtom } from "jotai";
import { Row, Col, Select } from "antd";
import { datasetAtom } from "@/state";
import DataModal from "@/component/modal/DataModal";
import LabelTable from "@/component/table/LabelTable";
import DataTable from "@/component/table/DataTable";

const DataPage: React.FC = () => {
  const [dataset] = useAtom(datasetAtom);
  const [datasetId, setDatasetId] = useState<number>(); // 当前数据集
  const [force, setForce] = useState<any>({});

  useEffect(() => {
    if (!datasetId && dataset.length) {
      setDatasetId(dataset[0].id);
    }
  }, [datasetId, dataset]);

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

        <Col>
          <DataModal onChange={() => setForce({})} />
        </Col>
      </Row>

      <div className="table-box">
        <h2>数据列表</h2>

        <div style={{ marginBottom: 20 }}>
          <LabelTable datasetId={datasetId!} force={force} />
        </div>

        <DataTable
          datasetId={datasetId!}
          force={force}
          onChange={() => setForce({})}
        />
      </div>
    </div>
  );
};

export default DataPage;
