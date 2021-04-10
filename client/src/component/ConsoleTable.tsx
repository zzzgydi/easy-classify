import React, { useEffect, useRef } from "react";
import { Tag } from "antd";

interface ConsoleTableProps {
  results: {
    time: string;
    items: {
      labels: string[];
      scores: number[];
    }[];
  }[];
}

const EachLabel: React.FC<any> = (props) => {
  const { label, score } = props;

  const showScore = `(${(score * 100).toPrecision(4)}%)`;

  return (
    <Tag className="each-label">
      <span>{label}&ensp;</span>
      <span className="possible">{showScore}</span>
    </Tag>
  );
};

const ConsoleTable: React.FC<ConsoleTableProps> = (props) => {
  const { results } = props;

  const domRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    domRef.current?.scrollTo({ top: 999999999, behavior: "smooth" });
  }, [results]);

  return (
    <div className="console-table" ref={domRef}>
      {results.map(({ time, items }, index) => (
        // 每一次预测
        <div key={index} className="each-result">
          <span>{time}</span>

          <div>
            {items.map((item, idx) => (
              // 每一次预测的每一项
              <div key={idx} className="each-item">
                <span className="each-item__idx">{idx + 1}</span>

                {item.labels.map((label, i) => (
                  <EachLabel key={i} label={label} score={item.scores[i]} />
                ))}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default ConsoleTable;
