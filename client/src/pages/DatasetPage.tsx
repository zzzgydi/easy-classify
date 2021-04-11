import React, { useState } from "react";
import DatasetModal from "../component/DatasetModal";
import DatasetTable from "../component/DatasetTable";
import datasetApi from "../service/dataset";

const DatasetPage: React.FC = () => {
  const [force, setForce] = useState<any>({});

  return (
    <div className="dataset-page">
      <div className="main-box">
        <header>
          <DatasetModal onChange={() => setForce({})} />
        </header>

        <main>
          <DatasetTable force={force} />
        </main>
      </div>
    </div>
  );
};

export default DatasetPage;
