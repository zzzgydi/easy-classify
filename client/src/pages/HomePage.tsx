import React, { useEffect } from "react";
import { Button, Col, Input, message, Row, Select } from "antd";
import { atom, useAtom } from "jotai";
import { apiApplyModel } from "@/service/model";
import ConsoleTable from "@/component/ConsoleTable";

const test = `mens ultrasheer: This model may be ok for sedentary types, but I'm active and get around alot in my job - consistently found these stockings rolled up down by my ankles! Not Good!! Solution: go with the standard compression stocking, 20-30, stock #114622. Excellent support, stays up and gives me what I need. Both pair of these also tore as I struggled to pull them up all the time. Good riddance/bad investment!`;

const atomName = atom<string>(null! as string); // 选择的模型名称
const atomModels = atom<string[]>([]);
const atomPredictText = atom<string>(test);
const atomPredResults = atom<any[]>([]);

const HomePage: React.FC = () => {
  const [name, setName] = useAtom(atomName);
  const [models, setModels] = useAtom(atomModels);
  const [predictText, setPredictText] = useAtom(atomPredictText);
  const [predResults, setPredResults] = useAtom(atomPredResults);

  useEffect(() => {
    // apiGetModel().then((res) => {
    //   setModels(res.result || []);
    // });
  }, []);

  const onPredict = () => {
    if (!name) {
      message.error("必须选择模型");
      return;
    }
    if (!predictText) {
      message.error("请输入预测文本");
      return;
    }
    const data = predictText.split("\n").filter((e) => e && e.trim());

    apiApplyModel(name, data, 3).then((res) => {
      const { result = [] } = res;
      const now = new Date();
      const hour = now.getHours().toString().padStart(2, "0");
      const min = now.getMinutes().toString().padStart(2, "0");
      const sec = now.getSeconds().toString().padStart(2, "0");
      const time = `${hour}:${min}:${sec}`;

      const results = {
        time,
        items: result.map((item: any) => ({
          ...item,
          labels: item.labels.map((label: string) =>
            label.replace("__label__", "")
          ),
        })),
      };
      setPredResults((newRes) => [...newRes].concat(results));
    });
  };

  return (
    <div className="home-page">
      <Row className="operate-box">
        <Col flex="1 1 150px">
          <span>选择模型：</span>
          <Select
            value={name}
            onChange={(val) => setName(val)}
            placeholder="请选择使用的模型"
            style={{ width: "calc(100% - 85px)", maxWidth: 200 }}
            options={models.map((v) => ({ label: v, value: v }))}
          />
        </Col>

        <Col>
          <Button type="primary" onClick={onPredict}>
            预测
          </Button>
        </Col>
      </Row>

      <div className="content-box">
        <h2>预测文本</h2>
        <Input.TextArea
          rows={10}
          value={predictText}
          placeholder="换行输入多行预测文本"
          onChange={({ target }) => setPredictText(target.value)}
        />
      </div>

      <div className="result-box">
        <h2>预测结果</h2>
        <ConsoleTable results={predResults} />
      </div>
    </div>
  );
};

export default HomePage;
