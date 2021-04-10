import { Tag } from "antd";
import React, { useEffect, useState } from "react";
import { apiGetLabel } from "../service/dataset";

interface LabelTableProps {
  name: string;
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
  const { name, force } = props;

  const [labels, setLabels] = useState<[string, number][]>([]);

  useEffect(() => {
    if (!name) return;
    apiGetLabel(name).then((res) => {
      setLabels(res.result);
    });
  }, [name, force]);

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
