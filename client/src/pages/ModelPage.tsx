import React from "react";
import { useAtom } from "jotai";
import { updateModelAtom } from "@/state";
import TrainModal from "@/component/modal/TrainModal";
import ModelTable from "@/component/table/ModelTable";
import { Button, Space } from "antd";

const ModelPage: React.FC = () => {
  const [, updateModel] = useAtom(updateModelAtom);

  return (
    <div className="model-page">
      <div className="header-box">
        <div className="title">模型管理</div>

        <Space size="middle">
          <Button onClick={() => updateModel(true)}>刷新</Button>
          <TrainModal />
        </Space>
      </div>

      <div className="main-box">
        <ModelTable />
      </div>
    </div>
  );
};

export default ModelPage;
