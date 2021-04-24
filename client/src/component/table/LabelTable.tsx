import { Tag } from "antd";
import React, { useEffect, useState } from "react";
import labeldataApi from "@/service/labeldata";

interface LabelTableProps {
  datasetId: number;
  force: any;
}

const COLORS = [
  "magenta",
  "geekblue",
  "orange",
  "gold",
  "purple",
  "red",
  "green",
];

const LabelTable: React.FC<LabelTableProps> = (props) => {
  const { datasetId, force } = props;

  const [labels, setLabels] = useState<[string, number][]>([]);

  useEffect(() => {
    if (!datasetId) return;
    labeldataApi.labels(datasetId).then((res: any) => {
      setLabels(res.result);
    });
  }, [datasetId, force]);

  return (
    <div>
      {labels.map((label, index) => (
        <Tag
          key={label[0]}
          color={COLORS[index % COLORS.length]}
        >{`${label[0]} [${label[1]}]`}</Tag>
      ))}
    </div>
  );
};

export default LabelTable;
